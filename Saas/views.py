from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.urls import reverse_lazy
from .models import CV


class CVView(TemplateView):
    model = CV
    template_name = 'Saas/index.html'
    context_object_name = 'cv'


class AboutView(TemplateView):
    template_name = 'Saas/about.html'


class CreateCvView(LoginRequiredMixin, TemplateView):
    template_name = 'Saas/create-cv.html'
    login_url = '/login/'


class ModeleView(TemplateView):
    template_name = 'Saas/modeles.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'Saas/register.html'
    success_url = reverse_lazy('profile')

    def dispatch(self, request, *args, **kwargs):
        # Redirige si déjà connecté
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Compte créé avec succès. Bienvenue !')
        return response


class LoginView(TemplateView):
    template_name = 'Saas/login.html'

    def dispatch(self, request, *args, **kwargs):
        # Redirige si déjà connecté
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthenticationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Connexion réussie.')
            # Redirige vers next si présent, sinon profile
            next_url = request.GET.get('next', '/profile/')
            return redirect(next_url)
        return render(request, self.template_name, {'form': form})


class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('cv')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'Saas/profile.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cvs'] = CV.objects.filter(user=self.request.user) if hasattr(CV, 'user') else []
        context['cv_count'] = len(context['cvs'])
        context['download_count'] = 0
        context['best_score'] = '—'
        return context

    def post(self, request, *args, **kwargs):
        user = request.user

        # Infos de base
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name  = request.POST.get('last_name',  user.last_name)
        user.email      = request.POST.get('email',      user.email)

        # Nom d'utilisateur — vérifie unicité
        new_username = request.POST.get('username', user.username)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if new_username != user.username and User.objects.filter(username=new_username).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà pris.')
            return self.get(request, *args, **kwargs)
        user.username = new_username

        # Changement de mot de passe (optionnel)
        pw1 = request.POST.get('new_password1', '')
        pw2 = request.POST.get('new_password2', '')
        if pw1 or pw2:
            if pw1 != pw2:
                messages.error(request, 'Les mots de passe ne correspondent pas.')
                return self.get(request, *args, **kwargs)
            if len(pw1) < 8:
                messages.error(request, 'Le mot de passe doit contenir au moins 8 caractères.')
                return self.get(request, *args, **kwargs)
            user.set_password(pw1)
            update_session_auth_hash(request, user)  # garde la session active

        user.save()
        messages.success(request, 'Profil mis à jour avec succès.')
        return redirect('profile')