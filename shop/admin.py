from django.contrib import admin
from .models import* 

# Register your models here.
class catagdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(categ,catagdmin)

class prodAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','available','img','stock']
    list_editable = ['img','price','available','stock']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(product,prodAdmin)
