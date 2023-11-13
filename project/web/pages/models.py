from django.db import models

# Create your models here.

class product (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=64)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name





