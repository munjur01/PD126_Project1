from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='user_info_images/')

    def __str__(self):
        return self.name
