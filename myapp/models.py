from django.db import models

# Create your models here.

class Quote(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=10)
    email = models.EmailField()
    product_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Logo(models.Model):
    logo = models.ImageField(upload_to="img/%y", default="")
    
class Cust_logo(models.Model):
    cust_logo = models.ImageField(upload_to='img/%y', default="")
    
class Why(models.Model):
    why = models.ImageField(upload_to="img/%y", default="")
    
class Happy_cust(models.Model):
    happy_cust = models.ImageField(upload_to="img/%y", default="")
    
class Prod_serv(models.Model):
    prod_serv = models.ImageField(upload_to="img/%y", default="")

class Round_neck(models.Model):
    round_neck = models.ImageField(upload_to="img/%y", default="")
    
class Polo(models.Model):
    polo = models.ImageField(upload_to="img/%y", default="")
    
class Jersey(models.Model):
    jersey = models.ImageField(upload_to="img/%y", default="")

class Hoodie(models.Model):
    hoodie = models.ImageField(upload_to="img/%y", default="")

class Cap(models.Model):
    cap = models.ImageField(upload_to="img/%y", default="")