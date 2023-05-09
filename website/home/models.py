from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank = True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    def __str__(self):
        return self.name
    @property
    def imageurl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
class producttail(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    def __str__(self):
        return self.name
class order(models.Model):
    customer = models.ForeignKey(customer, blank=True, on_delete=models.SET_NULL, null=True)
    data_order = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    tranactuon = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.id)
class orderitem(models.Model):
    product = models.ForeignKey(product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
class shippingaddress(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    def __str__(self):
        return self.address