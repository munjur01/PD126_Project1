
from django.shortcuts import render
from .models import UserInfo, Experience

def IndexView(request):
    user_info_data = UserInfo.objects.all()
    data = {
        'user_info': user_info_data
    }
    return render(request, 'index.html', context=data)

def ResumeView(request):
    job_info_data = Experience.objects.all()
    context = {
        'job_info_data': job_info_data
    }
    return render(request, 'resume.html', context)

def ProjectView(request):
    return render(request, 'projects.html')

def ContactView(request):
    return render(request, 'contact.html')
