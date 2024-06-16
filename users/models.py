from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.text import slugify






class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30,db_index=True)
    last_name  = models.CharField(max_length=30, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
           slug_value = f"{self.first_name}-{self.last_name}"
           self.slug = slugify(slug_value)
        super().save(*args, **kwargs)
    
    
       



    