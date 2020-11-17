from django.contrib import admin
from webapp.models import Computer
from webapp.forms import ComputerForm
# Register your models here.
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['computer_name','IP_address',
                    'MAC_address','user_name','purchase_date','timestamp']
    form = ComputerForm
    list_filter = ['computer_name','IP_address']
    search_fields = ['computer_name','IP_address']

admin.site.register(Computer,ComputerAdmin)