from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


# Create your models here.


class GetForm(models.Model):
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=16)
    date = models.DateField(max_length=10)
    text = models.TextField(max_length=100)
