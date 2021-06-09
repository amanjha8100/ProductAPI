from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.price}'