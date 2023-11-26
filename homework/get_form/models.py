from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


# Create your models here.


class GetForm(models.Model):
    email = models.EmailField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    date = models.DateField(max_length=10, blank=True, null=True)
    text = models.TextField(max_length=100, blank=True, null=True)
