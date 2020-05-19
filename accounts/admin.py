from django.contrib import admin

from .models import Customer,Products,Order,Tag

admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Tag)
