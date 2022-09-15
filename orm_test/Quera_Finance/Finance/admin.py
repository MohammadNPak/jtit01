from django.contrib import admin
from . import models

admin.site.register(models.Department)
admin.site.register(models.Payment)
admin.site.register(models.Salary)
admin.site.register(models.Employee)
admin.site.register(models.Attendance)
admin.site.register(models.Project)
admin.site.register(models.EmployeeProjectRelation)
admin.site.register(models.Payslip)
