from cgitb import text
from typing import Any
from django.db import models

# Create your models here.
class Posts(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user=models)
    Created_date = models.DateTimeField
    Published_date = models.DateTimeField
