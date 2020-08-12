from django.db import models

# Create your models here.
from django.contrib.auth.models import 
    (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class UserManager(BaseUserManager):
    
    def create_user(self, username, email, password=None):
        if username is None:
            raise ValueError("Users should have a username")
        if email is None:
            raise ValueError("Users should have a email")
        user = self.model(username=username, email=self.nomalize_email(email))
        user.set_password(password)
        user.save()

    def create_superuser(self, username, email, password):
        if password is None:
            raise ValueError("Password should not be None")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstracBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.CharField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def token(self):
        return ''

