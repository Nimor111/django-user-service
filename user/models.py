from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    USER = 'USER'
    ADMINISTRATOR = 'ADMINISTRATOR'

    ROLE_CHOICES = (
        ('user', 'user'),
        ('administrator', 'administrator')
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=50)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user'
    )

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        return super().save(*args, **kwargs)
