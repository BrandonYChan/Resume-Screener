from django.urls import path
from . import views

urlpatterns = [
    path('gradio/', views.gradio_embed, name='gradio_embed'), 
    path('save-input/', views.save_gradio_input, name='save_gradio_input'), 
]