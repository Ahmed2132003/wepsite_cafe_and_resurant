from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('order_summary/', views.order_summary_view, name='order_summary'),
    path('order_summary/<int:item_id>/', views.order_summary_with_item, name='order_summary_with_item'),
]
