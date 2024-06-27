
from django.contrib import admin
from django.urls import path
from myapp.views import IndexView, ResumeView, ProjectView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name='index'),
    path('resume/', ResumeView, name='resume'),
    path('projects/', ProjectView, name='projects'),
    path('contact/', ContactView, name='contact'),
]
