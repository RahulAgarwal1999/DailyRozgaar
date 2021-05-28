from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('customerindex',views.customerindex,name='customerindex'),
]
