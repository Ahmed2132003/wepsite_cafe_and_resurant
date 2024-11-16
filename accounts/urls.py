from django.urls import path
from . import views
from .views import daily_report, add_expense
app_name = 'accounts'
urlpatterns = [
    # رابط التقرير اليومي
    path('daily_report/', views.daily_report, name='daily_report'),
    path('add_expense/', add_expense, name='add_expense'),
]
