from django.contrib import admin
from Api.models import CompanyModel,EmployeeModel
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','active')
    search_fields=('name',)

class EmployeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',)

admin.site.register(CompanyModel,CompanyAdmin)
admin.site.register(EmployeeModel,EmployeAdmin)

# admin user name password
# moizkhan
# moiz@123
