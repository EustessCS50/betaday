from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_of_business = models.CharField(max_length=255)