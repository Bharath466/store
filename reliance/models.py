from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Out Door','Out Door')
    )
    name=models.CharField(max_length=100)
    price=models.IntegerField(max_length=5)
    category=models.CharField(max_length=10,choices=CATEGORY)
    description=models.CharField(max_length=500)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered')
    )
    date_created=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=STATUS)
    