
from django.shortcuts import render

def IndexView(request):
    return render(request, 'index.html')

def ResumeView(request):
    return render(request, 'resume.html')

def ProjectView(request):
    return render(request, 'projects.html')

def ContactView(request):
    return render(request, 'contact.html')
