# accounts/forms.py
from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'description', 'amount']  # الحقول التي تريد أن تظهر في النموذج