from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item', views.item, name='item'),
    path('bill', views.bill, name='bill'),
    path('invoice', views.invoice, name='invoice'),
    path('marks', views.marks, name='marks'),
    path('duplicate', views.duplicate, name='duplicate'),
]