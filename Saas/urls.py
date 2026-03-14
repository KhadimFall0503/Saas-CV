from django.urls import path
from .views import CVView, AboutView, CreateCvView

urlpatterns = [
    path('', CVView.as_view(), name='cv'),
    path('about/', AboutView.as_view(), name='about'),
    path('create-cv/', CreateCvView.as_view(), name='create-cv'),
]