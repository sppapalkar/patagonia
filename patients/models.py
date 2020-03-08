from django.conf import settings
from django.db import models
from django.urls import reverse


class Patient(models.Model):
    first_name = models.CharField(blank=False, max_length=30, verbose_name='first name')
    last_name = models.CharField(blank=False, max_length=30, verbose_name='last name')
    email = models.EmailField(blank=False, unique=True, verbose_name='email address')
    date_created = models.DateTimeField(auto_now_add=True)
    physician = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('patients-index')


