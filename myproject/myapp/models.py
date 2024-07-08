from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='user_info_images/')

    class Meta:
        verbose_name_plural = 'UserInfo'

    def __str__(self):
        return self.name

class Experience(models.Model):
    job_year = models.CharField(max_length=200)
    job_title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.job_title

class ContactInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.name