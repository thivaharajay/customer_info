from django.db import models

# Create your models here.

class product_details(models.Model):
    productName = models.TextField(null=True)
    produtID= models.IntegerField(null=True)
    Category=models.TextField(null=True)