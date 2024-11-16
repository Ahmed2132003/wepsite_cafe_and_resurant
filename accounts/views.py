# accounts/views.py
from django.shortcuts import render
from orders.models import Order
from .models import Expense
from django.db.models import Sum
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import ExpenseForm

def daily_report(request):
    today = timezone.now().date()
    total_sales = Order.objects.filter(created_at__date=today, is_completed=True).aggregate(Sum('total_price'))['total_price__sum'] or 0
    total_expenses = Expense.objects.filter(created_at__date=today).aggregate(Sum('amount'))['amount__sum'] or 0
    profit = total_sales - total_expenses
    total_orders = Order.objects.filter(created_at__date=today).count()

    context = {
        'total_sales': total_sales,
        'total_expenses': total_expenses,
        'profit': profit,
        'total_orders': total_orders,
    }
    return render(request, 'accounts/daily_report.html', context)
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()  # حفظ المصاريف الجديدة
            return redirect('accounts:daily_report')  # إعادة توجيه إلى صفحة التقرير اليومي
    else:
        form = ExpenseForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/add_expense.html', context)
