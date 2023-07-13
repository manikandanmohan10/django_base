import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User,PermissionsMixin,BaseUserManager, AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.

# class UserManager(BaseUserManager):

class User(AbstractUser):
    __tablename__ = 'tabUser'
    
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    email = models.EmailField(blank=False)

    def get_tokens(self):
        refresh_token = RefreshToken.for_user(self)
        token = {
                    'refresh': str(refresh_token),
                    'access': str(refresh_token.access_token),
                }
        
        return token


class Book(models.Model):
    __tablename__ = 'tabBook'