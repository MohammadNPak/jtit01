from django.db import models
from django.contrib.auth.models import User
 

class Department(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Payment(models.Model):
    SALARY = 's'
    PAYMENT_TYPES = (
        (SALARY, 'Salary'),
    )
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    account_number = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=1, choices=PAYMENT_TYPES)

    def __str__(self):
        return self.description


class Employee(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.account.username


class Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    base = models.DecimalField(max_digits=6, decimal_places=2)
    tax = models.DecimalField(max_digits=3, decimal_places=1)
    insurance = models.DecimalField(max_digits=3, decimal_places=1)
    overtime = models.PositiveIntegerField()

    def __str__(self):
        return self.employee.account.username


class Payslip(models.Model):
    base = models.DecimalField(max_digits=6, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    insurance = models.DecimalField(max_digits=5, decimal_places=2)
    overtime = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, null=True,
                                   blank=True)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    in_time = models.TimeField(null=True, blank=True)
    out_time = models.TimeField(null=True, blank=True)
    late_cause = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.employee, self.date.strftime("%b %d %Y"))


class Project(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employees = models.ManyToManyField(Employee, through='EmployeeProjectRelation')
    estimated_end_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title


class EmployeeProjectRelation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hours = models.PositiveIntegerField()
    role = models.CharField(max_length=100)

    def __str__(self):
        return '{} : project {}'.format(self.employee, self.project)
