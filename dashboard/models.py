from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=20, unique=True, db_index=True)
    flag = models.ImageField(upload_to='flags/')
    code = models.CharField(max_length=10,unique=True)

class Language(models.Model):
    name = models.CharField(max_length=20, unique=True, db_index=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='languages')