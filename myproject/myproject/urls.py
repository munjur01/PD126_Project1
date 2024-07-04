
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from myapp.views import IndexView, ResumeView, ProjectView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name='index'),
    path('resume/', ResumeView, name='resume'),
    path('projects/', ProjectView, name='projects'),
    path('contact/', ContactView, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)