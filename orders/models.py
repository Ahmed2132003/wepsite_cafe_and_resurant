# orders/models.py
from django.db import models
from menu.models import MenuItem

class Order(models.Model):
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.menu_item.price * self.quantity
