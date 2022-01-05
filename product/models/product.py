
from django.db import models



class Product(models.Model):

    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.TextField(max_length=200, null=False, default="NA")
    description = models.CharField( max_length=700,null=False, default="NA")
    price = models.FloatField( null=False, default='0.00')
    stock = models.BooleanField(null=False, default=True)
    image = models.ImageField(upload_to='media/upload', default="NA")
