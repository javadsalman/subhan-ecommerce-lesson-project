from django.db import models

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
    ('not_paid', 'Not paid')
] 


class Coupon(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank=True)
    discount_percent = models.IntegerField()
    expire_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    code = models.CharField(max_length=100)
    used_users = models.ManyToManyField("auth.User")
    created = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=100)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()