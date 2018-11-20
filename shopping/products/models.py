from django.db import models

# Create your models here.

class product_details(models.Model):
    productName = models.TextField(null=True)
    volPlus= models.IntegerField(null=True)
    volUNLD = models.IntegerField(null=True)
    volSUPER = models.IntegerField(null=True)
    SUPER = models.IntegerField(null=True)
    volCDIESEL = models.IntegerField(null=True)
    CDIESEL = models.IntegerField(null=True)
    volRDIESEL = models.IntegerField(null=True)
    RDIESEL = models.IntegerField(null=True)
    OIL = models.IntegerField(null=True)
    MISC = models.IntegerField(null=True)
    TAX = models.IntegerField(null=True)
    AMT_TOTAL = models.IntegerField(null=True)

class customer(models.Model):
    customerName = models.TextField(null=True)
    phoneNumber = models.IntegerField(null=True)
    address = models.TextField(null=True)
    pinCode = models.IntegerField(null=True)