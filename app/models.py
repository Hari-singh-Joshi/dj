from django.db import models
CATEGORY_CHOICES = [
        ('ELECTRONICS', 'Electronics'),
        ('CLOTHING', 'Clothing'),
        ('FOOD', 'Food'),
        ('FURNITURE', 'Furniture'),
        ('OTHER', 'Other'),
    ]
class Product(models.Model):
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='OTHER')
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} ({self.sku})"