from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StockDetail(models.Model):
    stock = models.CharField(max_length=255, unique=True)
    user = models.ManyToManyField(User)