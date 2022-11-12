from django.db import models
from django.contrib.auth.models import User
# from .modelsDB import TYPES
 
class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    weight=models.IntegerField(null=True)
    image = models.ImageField(null=True, blank=True)
    type = models.CharField(max_length=50, null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)
    amount= models.IntegerField()


    # fields =['_id','desc','price']
    def __str__(self):
        return self.desc


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    # address = models.CharField(max_length=300)
    # mobile_phone = models.CharField(max_length=16)
    total = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)
    createdTime=models.DateTimeField(auto_now_add=True)
    


class Order_det(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    order_id =models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    prod_id =models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    amount= models.IntegerField()
    total = models.IntegerField()



