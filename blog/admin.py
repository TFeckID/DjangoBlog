from django.contrib import admin
from .models import Artical
# Register your models here.

class ArticalAdmin(admin.ModelAdmin):
    list_display = ['title','category','pub_date','update_date']

admin.site.register(Artical,ArticalAdmin)