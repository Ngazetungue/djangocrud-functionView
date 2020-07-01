from django.db import models

# Create your models here.
class Products(models.Model):
    descriptions = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.descriptions

