from django.db import models

from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)             # Integer primary key
    name = models.CharField(max_length=255)             # Product name with max length 255 characters
    price = models.FloatField()                         # Price as a float
    available = models.BooleanField(default=True)       # Availability status (True by default)

    def __str__(self):
        return self.name

