from django.shortcuts import render, redirect
from .models import MenuItem
from orders.forms import OrderItemForm
from orders.models import Order, OrderItem

def menu_view(request):
    menu_items = MenuItem.objects.filter(available=True)
    order_form = OrderItemForm()

    if request.method == 'POST':
        order_form = OrderItemForm(request.POST)
        if order_form.is_valid():
            order_item = order_form.save(commit=False)

            # محاولة الحصول على الطلب المفتوح في الجلسة الحالية أو إنشاء طلب جديد
            order_id = request.session.get('order_id')
            if order_id:
                order = Order.objects.filter(id=order_id, is_completed=False).first()
            else:
                order = None

            # إذا لم يتم العثور على الطلب، قم بإنشاء طلب جديد
            if not order:
                order = Order.objects.create()
                request.session['order_id'] = order.id

            # إضافة العنصر إلى الطلب
            order_item.order = order
            order_item.save()
            
            # تحديث إجمالي السعر للطلب
            order.total_price += order_item.get_cost()
            order.save()

            # إعادة التوجيه إلى صفحة الفاتورة (الملخص) بعد إضافة العنصر
            return redirect('order_summary')  # إعادة التوجيه إلى صفحة الفاتورة

    context = {
        'menu_items': menu_items,
        'order_form': order_form
    }
    return render(request, 'menu/menu.html', context)
