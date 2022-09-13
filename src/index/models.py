from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField(default=0)

    def __set__(self, instance, value):
        return self.name

    def get_price_usd(self):
        return "{0:.2f}".format(self.price / 100)

class Order(models.Model):
    pass

class Discount(models.Model):
    pass