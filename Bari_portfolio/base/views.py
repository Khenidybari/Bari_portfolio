from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def cms(request):
    return render(request, 'cms.html')

def personal(request):
    return render(request, 'personal.html')

def skills(request):
    return render(request, 'skills.html')

def projects(request):
    return render(request, 'projects.html')