from django.urls import path
from . import views

urlpatterns = [
    path('loginworker',views.loginworker,name='loginworker'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('loginadmin',views.loginadmin,name='loginadmin'),
    path('registeruser',views.registeruser,name='registeruser'),
    path('registerworker',views.registerworker,name='registerworker'),
    path('dashboarduser',views.dashboarduser,name='dashboarduser'),
    path('dashboardworker',views.dashboardworker,name='dashboardworker'),
    path('logout',views.logout,name='logout'),
    path('accountsettingsworker',views.accountsettingsworker,name='accountsettingsworker'),
    path('accountsettingsuser',views.accountsettingsuser,name='accountsettingsuser'),
    path('dashboardadmin',views.dashboardadmin,name='dashboardadmin'),
    path('adminrfqreceived',views.adminrfqreceived,name='adminrfqreceived')
]
