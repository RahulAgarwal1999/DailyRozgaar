from django.urls import path
from . import views

urlpatterns = [

    path('loginadmin',views.loginadmin,name='loginadmin'),
    path('dashboardadmin',views.dashboardadmin,name='dashboardadmin'),
    path('adminrfqreceived',views.adminrfqreceived,name='adminrfqreceived'),

    path('loginuser',views.loginuser,name='loginuser'),
    path('registeruser',views.registeruser,name='registeruser'),
    path('dashboarduser',views.dashboarduser,name='dashboarduser'),
    path('user_history',views.userHistory,name='user_history'),
    path('accountsettingsuser',views.accountsettingsuser,name='accountsettingsuser'),

    path('loginworker',views.loginworker,name='loginworker'),
    path('registerworker',views.registerworker,name='registerworker'),
    path('dashboardworker',views.dashboardworker,name='dashboardworker'),
    path('accountsettingsworker',views.accountsettingsworker,name='accountsettingsworker'),
    path('worker_feedback',views.workerfeedback,name='workerfeedback'),

    path('logout',views.logout,name='logout'),

]
