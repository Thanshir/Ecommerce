from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.IntegerField()
    description=models.TextField(max_length=500)


    def __str__(self):
        return self.name
    

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=100, default="")
    subcategory=models.CharField(max_length=100, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=200)
    image=models.ImageField(upload_to='products/images')

    
    def __str__(self):
        return self.product_name
    

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=200)
    city=models.CharField(max_length=80)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=50)
    oid=models.CharField(max_length=100, blank=True)
    amountpaid=models.CharField(max_length=500, blank=True, null=True)
    paymentstatus=models.CharField(max_length=20, blank=True)
    phone=models.CharField(max_length=10, default="")

    def __str__(self):
        return self.name
    

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=500)
    deliveried=models.BooleanField(default=False)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."
