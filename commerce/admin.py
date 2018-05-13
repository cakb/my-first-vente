from django.contrib import admin
from commerce.models import *




class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline
    ]     
    
class OrderInline(admin.TabularInline):
   model=Order
   readonly_fields=["created_at","contacted","product"]
class ContactAdmin(admin.ModelAdmin):
    inlines= [
        OrderInline
        ]

class OrderAdmin(admin.ModelAdmin):
    list_filter=("created_at","contacted")
    readonly_fields=["created_at","contact","product","contacted"]
  

admin.site.register(Product, ProductAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Order,OrderAdmin)



