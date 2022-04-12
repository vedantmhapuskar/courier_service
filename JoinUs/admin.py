from django.contrib import admin

from JoinUs.models import jobapp

# Register your models here.
@admin.register(jobapp)
class jobadmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','email', 'phonenumber', 'city','empstatus', 'resume']