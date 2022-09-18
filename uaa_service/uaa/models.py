from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Role(TimeStamp):
    role_name = models.CharField(max_length=20)

    def __str__(self):
        return self.role_name

class User(AbstractUser):
    role = models.ForeignKey(Role, blank=True,null=True,related_name="role_names",on_delete=models.SET_NULL)
    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")
    empNo = models.CharField(max_length=15,null=True,blank=True)

    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"


# from django.conf import settings
# from django.db import models

# class Article(models.Model):
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )