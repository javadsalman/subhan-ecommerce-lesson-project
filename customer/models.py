from django.db import models

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.PROTECT)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    deleted = models.BooleanField(default=False)