from django.urls import path
from . import views

urlpatterns = [
    path('loginworker',views.loginworker,name='loginworker'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('registeruser',views.registeruser,name='registeruser'),
    path('registerworker',views.registerworker,name='registerworker'),
<<<<<<< HEAD
    path('dashboardworker',views.dashboardworker,name='dashboardworker'),
    path('dashboardcustomer',views.dashboardcustomer,name='dashboardcustomer'),
=======
    path('dashboarduser',views.dashboarduser,name='dashboarduser'),
    path('dashboardworker',views.dashboardworker,name='dashboardworker')
>>>>>>> 05af42a8474322eff7eea4e8392ae5a4b308b420
]
