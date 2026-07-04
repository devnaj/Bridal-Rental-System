from django.contrib import admin
from .models import Category, Product, Booking

# 1. Branding Customization
admin.site.site_header = "Aura Bridal Management Portal"
admin.site.site_title = "Aura Bridal Admin"
admin.site.index_title = "Inventory & Sustainability Dashboard"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'rental_price')
    list_editable = ('status',)
    list_filter = ('status', 'category')
    search_fields = ('name', 'description')

    # 2. Injecting Custom CSS
    class Media:
        css = {
            'all': ('rentals/css/admin_custom.css',)
        }

admin.site.register(Category)
admin.site.register(Booking)