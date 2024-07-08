from django.shortcuts import render, redirect
from .models import UserInfo, Experience
from .forms import ContactForm

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
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {'form': form})
