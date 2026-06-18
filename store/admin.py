from django.contrib import admin
from .models import Product, Cart, CartItem, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display  = ['order_id', 'user', 'status', 'total', 'created_at']
    list_editable = ['status']
    inlines       = [OrderItemInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ['name', 'price', 'stock']
    list_editable = ['stock']

admin.site.register(Cart)
admin.site.register(CartItem)