from django.db import models

# Create your models here.
class tbl_registraion(models.Model):
    username= models.CharField(max_length=200, null=True)
    password= models.CharField(max_length=200, null=True)
    confirm= models.CharField(max_length=200, null=True)

class tbl_application(models.Model):
    name= models.CharField(max_length=200, null=True)
    dob = models.DateField( null=True)
    age = models.IntegerField( null=True)
    gender = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.IntegerField( null=True)
    email = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    account = models.CharField(max_length=200, null=True)
    debit = models.CharField(max_length=200, null=True)
    credit = models.CharField(max_length=200, null=True)
    cheque = models.CharField(max_length=200, null=True)



