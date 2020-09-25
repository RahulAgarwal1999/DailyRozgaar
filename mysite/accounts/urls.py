from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('registercustomer',views.registercustomer,name='registercustomer'),
    path('registermanufacturer',views.registermanufacturer,name='registermanufacturer'),
]
