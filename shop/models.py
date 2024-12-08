from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class TitleAbstract(models.Model):
    title_az = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

class Campaign(TitleAbstract):
    discount = models.IntegerField()
    slider = models.BooleanField(default=False)

    

class Category(TitleAbstract):
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

class Color(TitleAbstract):
    pass

class Size(models.Model):
    title = models.CharField(10)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Product(TitleAbstract):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    campaign = models.ManyToManyField(Campaign)

class ProductImage(models.Model):
    image_file = models.ImageField(upload_to='product-images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    

class Review(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

