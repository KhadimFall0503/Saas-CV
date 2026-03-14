from django.shortcuts import render
from django.views.generic import TemplateView
from .models import CV

# Create your views here.
class CVView(TemplateView):
    model = CV
    template_name = 'Saas/index.html'
    context_object_name = 'cv'
    
class AboutView(TemplateView):
    template_name = 'Saas/about.html'

class CreateCvView(TemplateView):
    template_name = 'Saas/create-cv.html'
    
