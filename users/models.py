from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.forms import ValidationError
from django.utils.text import slugify






class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30,db_index=True)
    last_name  = models.CharField(max_length=30, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.slug:
           slug_value = f"{self.first_name}-{self.last_name}"
           self.slug = slugify(slug_value)
        super().save(*args, **kwargs)

class Profile(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, unique=True)
    is_phone_set = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_mfa_enable = models.BooleanField(default=False)
    image = models.ImageField(upload_to='users')

class Address(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='addresses')
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    is_primary = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['is_primary'],
                condition=models.Q(is_primary=True),
                name='unique_primary_address_per_user'
            )
        ]

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.state}, {self.country} - {self.postal_code}'

    def clean(self):
        if self.is_primary:
            primary_address = Address.objects.filter(user=self.user, is_primary=True).exclude(id=self.id)
            if primary_address.exists():
                raise ValidationError('There can be only one primary address per profile.')

    def save(self, *args, **kwargs):
        self.clean()
        if not self.slug:
            self.slug = slugify(self.street_address)
        super().save(*args, **kwargs)
       

    
    
       



    