from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse
from .models import GradioInput
import json 

def gradio_embed(request):
    return render(request, 'gradioapp/gradio_embed.html')

def save_gradio_input(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')  # Extract the input field value
        if name:
            GradioInput.objects.create(name=name)  # Save to database
            return JsonResponse({'message': 'Input saved successfully'})
        return JsonResponse({'error': 'Invalid data'}, status=400)
    
    