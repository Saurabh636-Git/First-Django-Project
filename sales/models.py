from django.db.models.deletion import CASCADE
from django.forms.utils import to_current_timezone
from django.db import models
import datetime
from .utils import gen_id

# Create your models here.

class Item(models.Model):
    item = models.CharField(max_length=30)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.item)


class Sale(models.Model):
    tr_id = models.CharField(max_length=12, blank=True)
    items = models.ForeignKey(Item, null=True, on_delete=CASCADE)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True)
    
    def save(self, *args, **kwargs):
        self.total = self.items.price * self.quantity
        if self.tr_id == "":
            self.tr_id = gen_id()
        return super().save(*args, **kwargs)
    

    def __str__(self):
        return str(self.tr_id)