from django.db import models

# Create your models here.

PRODUCT_CATEGORY = (
    ("Kitchen", "Kitchen"),
    ("Shoes", "Shoes"),
    ("Fashion", "Fashion"),
    ("Phone & Accessories", "Phone & Accessories")
)

class Product(models.Model):
    item = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(upload_to="Product-Images")
    description = models.TextField()
    category = models.CharField(max_length=200, choices=PRODUCT_CATEGORY)

    def __str__(self):
        return self.item
