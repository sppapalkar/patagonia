from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

alpha = RegexValidator(r'^[A-Za-z][A-Zsa-z\s]*$', 'Only alphabets and spaces are allowed.')


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(blank=False, max_length=30, verbose_name='first name', validators=[alpha])
    last_name = models.CharField(blank=False, max_length=30, verbose_name='last name', validators=[alpha])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email