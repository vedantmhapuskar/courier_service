from django.contrib import admin
from .models import packagedetails
# Register your models here.

@admin.register(packagedetails)
class packageadmin(admin.ModelAdmin):
    list_display = ['user','track_id','weight', 'slct1', 'slct2','city1','pincode1', 'state1','address1', 'city2','pincode2', 'state2','address2','accept', 'pickup', 'left','reach','shipped']

