from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage  # To upload Profile Picture
from django.urls import reverse
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .forms import *
from .models import *
from .filters import *
from twilio.rest import TwilioRestClient
from twilio.rest import Client
from school_management_system.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
from django.utils.html import strip_tags

def principaldashboard(request):
    all_student_count = Students.objects.all().count()
    staff_count = Staffs.objects.all().count()
    student_list = Students.objects.all()
    active_students = Students.objects.filter(stu_status="Active").count()
    Inactive_students = Students.objects.filter(stu_status="Inactive").count()
    staff_count = Staffs.objects.all().count()
    
    today = datetime.datetime.now()
    total_revenue = Revenue.objects.filter(
        created_date__year=today.year).aggregate(total_revenue=Sum('amount'))
    total_expenditure = Expenditure.objects.filter(
        created_date__year=today.year).aggregate(total_expenditure=Sum('amount'))
    
    acc_receivable = StudentBill.objects.all().aggregate(cc=Sum('balance'))
    expected_rev = StudentBill.objects.filter(
        bill_date__year=today.year).aggregate(cc=Sum('amount'))
    
    pending_pv = Pv.objects.filter(created_date__year=today.year,status="pending")
    approved_pv = Pv.objects.filter(created_date__year=today.year, status="approved")
    total_pending = Pv.objects.filter(created_date__year=today.year, status="pending").aggregate(cc=Sum('amount'))
    total_approved = Pv.objects.filter(created_date__year=today.year, status="approved").aggregate(cc=Sum('amount'))
    
    
    
    if total_revenue['total_revenue'] and not total_expenditure['total_expenditure']:
        expected_cash = total_revenue['total_revenue']
    elif not total_revenue['total_revenue'] and total_expenditure['total_expenditure']:
        expected_cash = -total_expenditure['total_expenditure']
    elif not total_revenue['total_revenue'] and not total_expenditure['total_expenditure']:
        expected_cash = 0.00
    else:
        expected_cash = total_revenue['total_revenue'] - \
            total_expenditure['total_expenditure']
    context ={
        'all_student_count': all_student_count,
        'student_list': student_list,
        'active_students': active_students,
        'Inactive_students':Inactive_students,
        'total_revenue': total_revenue,
        'total_expenditure': total_expenditure,
        'expected_cash': expected_cash,
        'staff_count': staff_count,
        'acc_receivable': acc_receivable,
        'expected_rev': expected_rev,
        'pending_pv': pending_pv,
        'approved_pv': approved_pv,
        'total_pending': total_pending,
        'total_approved': total_approved,
        
        
    }
    
    template='hod_template/principal.html'
    return render(request,template,context)
    
