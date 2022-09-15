
from django.db.models import F, Sum, Count, Case, When,Subquery,OuterRef
from .models import *


def query_0():
    q = Employee.objects.all()
    return q


def query_1():
    # TODO
    pass
    return ( Payslip.objects.filter(payment__isnull=True)
            .annotate(
                total_dept_employee=F('base') + F('tax') + F('insurance') + F('overtime'))
            .aggregate(total_dept=Sum('total_dept_employee')) )


def query_2(x):
    # TODO
    return Employee.objects.filter(salary__overtime__gte=x).aggregate(total_overtime=Sum('salary__payslip__overtime'))


def query_3():
    # TODO
    return Payment.objects.all().aggregate(total=Sum('amount'))


def query_4(x):
    # TODO
    return EmployeeProjectRelation.objects.filter(employee__id=x).aggregate(total_hours=Sum('hours'))


def query_5(x):
    # TODO
    return Employee.objects.annotate(total_payment=Sum('salary__payslip__payment__amount')).filter(total_payment__gt=x)


def query_6():
    # TODO
    #  Employee.objects.annotate(total_ours=Attendance.objects.filter(employee_id=OuterRef(id)).annotate(total_time=F('out_time')-F('in_time')).aggregate(Sum('total_time'))))


def query_7():
    # TODO
    pass


def query_8():
    # TODO
    pass


def query_9(x):
    # TODO
    pass


def query_10():
    # TODO
    pass
