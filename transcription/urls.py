from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # home page where file upload happens
    path('transcribe/', views.transcribe, name='transcribe'),  # endpoint to handle transcription
]
