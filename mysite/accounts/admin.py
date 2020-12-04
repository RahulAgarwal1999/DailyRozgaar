from django.contrib import admin
from .models import UserDetails,WorkerDetails,Service,ServiceHistory
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(WorkerDetails)
admin.site.register(Service)
admin.site.register(ServiceHistory)
