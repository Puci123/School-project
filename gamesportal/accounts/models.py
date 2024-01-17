from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.

class GPUser(AbstractUser):


    decryption      = models.TextField(default = "", blank = True, null = True)
    profile_picture = models.ImageField(upload_to='profilepictures/', default='profile_picture/No_Cover_Image.png') 

    def __str__(self):
        return self.username
    

