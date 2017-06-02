from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from leave.models import Employee

# Register your models here.

class EmployeeInline(admin.StackedInline):
	model = Employee
	verbose_name_plural = _('employee')

class UserAdmin(BaseUserAdmin):
	inlines = (EmployeeInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)