from django.db import models

# Create your models here.

class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    delegation_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.delegation_id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product_name}"


