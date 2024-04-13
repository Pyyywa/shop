from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'quantity_per_unit', 'category')
    search_fields = ('product_name',  'desc')
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    #list_display = ('id', 'category_name', 'description')
    list_display = ('id', 'category_name')

