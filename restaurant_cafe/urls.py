from django.contrib import admin
from django.urls import path , include
from menu import views as menu_views
from orders import views as order_views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', menu_views.menu_view, name='menu'),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')), 
]
