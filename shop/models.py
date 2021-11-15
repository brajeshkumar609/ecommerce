from django.db import models

# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.title
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount=models.FloatField()
    category=models.CharField(max_length=200)
    desc=models.TextField()
    image=models.CharField(max_length=200)

    class Meta:
        verbose_name = "Product"

class ring(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.CharField(max_length=200)

class order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    total = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Order"


