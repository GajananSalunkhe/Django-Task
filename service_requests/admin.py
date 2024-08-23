from django.contrib import admin

from django.contrib import admin
from .models import ServiceRequest, Customer

admin.site.register(ServiceRequest)
admin.site.register(Customer)

