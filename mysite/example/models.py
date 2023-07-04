from django.db import models

# Create your models here.
class Product_catogories(models.Model):
    catogory_name = models.CharField(max_length=200) 

    def __str__(self):
        return self.catogory_name

class Products(models.Model):
    catogory = models.ForeignKey(Product_catogories, related_name="products", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_cost = models.IntegerField()

    def __str__(self):
        return self.product_name