from django.db import models

# Create your models here.
class Chapter(models.Model):
    book = models.CharField("Book Name", max_length=240)
    words = models.IntegerField()
    created_date = models.DateField()