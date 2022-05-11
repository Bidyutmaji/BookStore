from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    rating = models.DecimalField( max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name