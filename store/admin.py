from django.contrib import admin
from .models import Category, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('category',)

class OrderItemInline(admin.TabularInline):

    model = OrderItem

    extra = 0 
 
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'customer_name',
        'user',
        'total_price',
        'payment_method',
         'status',
        'created_at'
    )
    inlines = [
        OrderItemInline
    ]

    search_fields = (
        'customer_name',
        'phone'
    )
    list_filter = (
    'status',
    'created_at'
    )