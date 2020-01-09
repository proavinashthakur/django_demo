from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField(default=0)
    feature = models.CharField(max_length=30)
    usage_status = models.CharField(max_length=25)
    kms_driven = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
