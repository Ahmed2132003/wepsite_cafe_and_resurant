# orders/forms.py
from django import forms
from .models import OrderItem

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1, 'value': 1}),
        }
