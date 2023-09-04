from django.contrib import admin
from .models import Product, Category, Color, Order


admin.site.register((Product, Category, Color, Order))
