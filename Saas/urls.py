from django.urls import path
from .views import (
    CVView, AboutView, CreateCvView, ModeleView,
    RegisterView, LoginView, LogoutView, ProfileView
)

urlpatterns = [
    path('',            CVView.as_view(),      name='cv'),
    path('about/',      AboutView.as_view(),   name='about'),
    path('create-cv/',  CreateCvView.as_view(), name='create-cv'),
    path('modeles/',    ModeleView.as_view(),   name='modeles'),
    

    # Auth
    path('login/',      LoginView.as_view(),    name='login'),
    path('logout/',     LogoutView.as_view(),   name='logout'),
    path('register/',   RegisterView.as_view(), name='register'),
    path('profile/',    ProfileView.as_view(),  name='profile'),
]