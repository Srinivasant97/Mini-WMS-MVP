from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here


class Inventory(models.Model):
    name = models.CharField(max_length=1)
    quantity = models.IntegerField(validators=[MinValueValidator(0),
                                               MaxValueValidator(5)])

    def __str__(self):
        return self.name


class order(models.Model):
    source = models.CharField(max_length=100)
    order_number = models.AutoField(primary_key=True)
    Lines = models.TextField(null=True)

    def __str__(self):
        return str(self.order_number)
