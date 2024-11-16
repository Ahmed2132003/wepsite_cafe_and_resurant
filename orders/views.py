# orders/views.py
from django.shortcuts import render, redirect
from .models import Order, OrderItem , MenuItem

def order_summary_view(request):
    order_id = request.session.get('order_id')
    if not order_id:
        return redirect('menu')  # إعادة التوجيه للمنيو إذا لم يكن هناك طلب

    order = Order.objects.get(id=order_id, is_completed=False)
    order_items = OrderItem.objects.filter(order=order)

    if request.method == 'POST':
        order.is_completed = True
        order.save()
        del request.session['order_id']
        return redirect('menu')

    context = {
        'order': order,
        'order_items': order_items
    }
    return render(request, 'orders/order_summary.html', context)

def order_summary_with_item(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    order_id = request.session.get('order_id')

    if not order_id:
        order = Order.objects.create()
        request.session['order_id'] = order.id
    else:
        order = Order.objects.get(id=order_id, is_completed=False)

    # تحديث الحقل هنا إلى 'menu_item' بدلاً من 'item'
    order_item = OrderItem.objects.create(order=order, menu_item=item, quantity=1)

    order.total_price += item.price
    order.save()

    return redirect('orders:order_summary')
