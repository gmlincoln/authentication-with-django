from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User_Model(AbstractUser):

    USER_TYPE  = [
        ('seeker','Job Seeker'),
        ('recruiter','Recruiter'),
    ]
    
    user_type = models.CharField(choices=USER_TYPE, max_length=100, null=True)

    