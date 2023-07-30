from django.db import models
from phonenumber_field.modelfields import   PhoneNumberField

# class Register(models.Models):
#     email = models.EmailField(max_length=254)
#     first_name = models.CharField(max_length= 100)
#     last_name = models.CharField(max_length=250)
#     phone = PhoneNumberField(null=False, blank=False, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)