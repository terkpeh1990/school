from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .import management
from .import staff
from .import principal
from .import parent

app_name = 'school'

urlpatterns = [
    path('add_student/<str:pk>/', management.add_student, name='add_student'),
    path('add_student_education_history', management.add_student_education,name='add_student_education_history'),
    path('add_student_emmergency_contact', management.add_student_emergency,name='add_student_emmergency_contact'),
    path('add_student_medical', management.add_student_medical,name='add_student_medical'),
    path('add_student_immunization', management.add_student_immunization, name='add_student_immunization'),
    path('next', management.nexts,name='next'),
    path('delete_student/<str:pk>/', management.delete_student, name='delete_student'),
    path('student_profile/<str:pk>/',management.student_profile, name='student_profile'),
    path('edit_student/<str:pk>/',management.edit_student, name='edit_student'),
   
    path('edit_student_edu/<str:pk>/', management.edit_student_education, name='edit_student_edu'),
    path('edit_student_emmergency/<str:pk>/',management.edit_student_emmergency, name='edit_student_emmergency'),
    path('edit_student_medical/<str:pk>/',management.edit_student_medical, name='edit_student_medical'),
    path('edit_student_immunization/<str:pk>/',management.edit_student_immunization, name='edit_student_immunization'),
    
    path('delete_student_education/<str:pk>/',management.delete_student_education, name='delete_student_education'),
    path('delete_student_emmergency/<str:pk>/',management.delete_student_emmergency, name='delete_student_emmergency'),
    path('delete_student_medical/<str:pk>/',management.delete_student_medical, name='delete_student_medical'),
    path('delete_student_immunization/<str:pk>/',management.delete_student_immunization,         name='delete_student_immunization'),
    
    path('add_profile_student_education/<str:pk>/',management.add_profile_student_education, name='add_profile_student_education'),
    path('add_profile_student_emmergency/<str:pk>/',
         management.add_profile_student_emmergency, name='add_profile_student_emmergency'),
    path('add_profile_student_medical/<str:pk>/',
         management.add_profile_student_medical, name='add_profile_student_medical'),
    path('add_profile_student_immunization/<str:pk>/',
         management.add_profile_student_immunization, name='add_profile_student_immunization'),
    
    
    path('add_staff', management.add_staff, name='add_staff'),
    path('add_staff_education_history', management.add_staff_education,name='add_staff_education_history'),
    path('add_staff_work_experience', management.add_staff_work_experience,name='add_staff_work_experience'),
    path('add_staff_emmergency_contact', management.add_staff_emmergency_contact,name='add_staff_emmergency_contact'),
    path('staff_profile/<str:pk>/',management.staff_profile, name='staff_profile'),
    path('staffnext', management.staffnexts, name='staffnext'),
    path('manage_staff', management.manage_staff, name='manage_staff'),
    
    path('edit_staff_edu/<str:pk>/',management.edit_staff_education, name='edit_staff_edu'),
    path('edit_staff_contact/<str:pk>/',management.edit_staff_emmergency, name='edit_staff_contact'),
    path('edit_staff_work/<str:pk>/',management.edit_staff_work, name='edit_staff_work'),
    
    path('delete_staff_education/<str:pk>/',management.delete_staff_education, name='delete_staff_education'),
    path('delete_staff_emmergency/<str:pk>/',management.delete_staff_emmergency, name='delete_staff_emmergency'),
    path('delete_staff_work/<str:pk>/',management.delete_staff_work, name='delete_staff_work'),
    
    path('add_profile_staff_education/<str:pk>/',management.add_profile_staff_education, name='add_profile_staff_education'),
    path('add_profile_staff_emmergency/<str:pk>/',
         management.add_profile_staff_emmergency, name='add_profile_staff_emmergency'),
    path('add_profile_staff_work/<str:pk>/',
         management.add_profile_staff_work, name='add_profile_staff_work'),
    path('edit_staff/<str:pk>/', management.edit_staff, name='edit_staff'),

    
    path('add_parent', management.add_parent, name='add_parent'),
    path('manage_parent', management.manage_parent, name='manage_parent'),
    path('manage_student', management.manage_student, name='manage_student'),
    path('edit_parent/<str:pk>/', management.edit_parent, name='edit_parent'),
    path('delete_parent/<str:pk>/', management.delete_parent, name='delete_parent'),
    
    
    path('add_academicyear', management.add_academicyear, name='add_academicyear'),
    path('manage_academicyear', management.manage_academicyear,name='manage_academicyear'),
    path('edit_academicyear/<str:pk>/',management.edit_academicyear, name='edit_academicyear'),
    path('delete_academic_year/<str:pk>/',management.delete_academic_year, name='delete_academic_year'),
    
    path('add_academicterm', management.add_academicterm, name='add_academicterm'),
    path('manage_academicterm', management.manage_academicterm, name='manage_academicterm'),
    path('edit_academicterm/<str:pk>/',management.edit_academicterm, name='edit_academicterm'),
    path('delete_academic_term/<str:pk>/',management.delete_academic_term, name='delete_academic_term'),
    
    path('add_class', management.add_class, name='add_class'),
    path('manage_class', management.manage_class, name='manage_class'),
    path('edit_class/<str:pk>/',management.edit_class, name='edit_class'),
    path('delete_class/<str:pk>/', management.delete_class, name='delete_class'),
    
    path('add_subject/<str:pk>/', management.add_subject, name='add_subject'),
    path('edit_subject/<str:pk>/', management.edit_subject, name='edit_subject'),
    path('delete_subject/<str:pk>/',management.delete_subject, name='delete_subject'),
    path('manage_subject', management.manage_subject, name='manage_subject'),
    
    path('create_attendance', staff.create_attendance,name='create_attendance'),
    path('manage_attendance', staff.manage_attendance, name='manage_attendance'),
    path('delete_attendance/<str:pk>/',staff.delete_attendance, name='delete_attendance'),
    path('edit_attendance/<str:pk>/',staff.edit_attendance, name='edit_attendance'),
    path('take_attendance/<str:pk>/',staff.take_attendance, name='take_attendance'),
    path('present/<str:pk>/',staff.present, name='present'),
    path('absent/<str:pk>/', staff.absent, name='absent'),
    path('closing', staff.closing, name='closing'),
    path('view_attendance/<str:pk>/',staff.view_attendance, name='view_attendance'),
    path('epresent/<str:pk>/', staff.epresent, name='epresent'),
    path('eabsent/<str:pk>/', staff.eabsent, name='eabsent'),
    
    path('create_results', staff.create_results, name='create_results'),
    path('manage_results', staff.manage_results, name='manage_results'),
    path('delete_results/<str:pk>/',staff.delete_results, name='delete_results'),
    path('edit_results/<str:pk>/',staff.edit_results, name='edit_results'),
    
    path('add_results/<str:pk>/', staff.add_results, name='add_results'),
    path('stud_results/<str:pk>/', staff.stud_results, name='stud_results'),
    path('subject_results/<str:pk>/',staff.subject_results, name='subject_results'),
    path('create_student_results/<str:pk>/',staff.create_student_results, name='create_student_results'),
    path('resultclose', staff.resultclose, name='resultclose'),
    path('view_student_result/<str:pk>/',staff.view_student_result, name='view_student_result'),
    path('print_student_result/<str:pk>/',
         staff.print_student_result, name='print_student_result'),
    path('add_promotion/<str:pk>/',staff.add_promotion, name='add_promotion'),
    
    
    path('create_bill', management.create_bill, name='create_bill'),
    path('manage_bill', management.manage_bill, name='manage_bill'),
    path('add_bill/<str:pk>/',management.add_bill, name='add_bill'),
    path('view_bill/<str:pk>/',management.view_bill, name='view_bill'),
    path('generate_student_bill/<str:pk>/',
         management.generate_student_bill, name='generate_student_bill'),
    path('parentbill/<str:pk>/', parent.parentbill,name='parentbill'),
    path('create_payroll', management.create_payroll, name='create_payroll'),
    path('manage_payroll',management.manage_payroll, name='manage_payroll'),
    path('run_payroll', management.run_payroll, name='run_payroll'),
    path('account_code', management.account_code, name='account_code'),
    path('editaccount_code/<str:pk>/',management.editaccount_code, name='editaccount_code'),
    path('manage_account_code', management.manage_account_code,
         name='manage_account_code'),
    
    path('manage_pv', management.manage_pv, name='manage_pv'),
    path('create_pv', management.create_pv, name='create_pv'),
    path('add_pv_details/<str:pk>/',management.add_pv_details, name='add_pv_details'),
    path('view_pv/<str:pk>/', management.view_pv, name='view_pv'),
    path('approve_pvs/<str:pk>/', management.approve_pvs, name='approve_pvs'),
    path('cancel_pvs/<str:pk>/', management.cancel_pvs, name='cancel_pvs'),
    
    path('make_payment/<str:pk>/', management.make_payment, name='make_payment'),
    
    path('totalrevenue', management.allrevenue, name="totalrevenue"),
    path('totalexpense', management.allexpenses, name="totalexpense"),
    path('income&expenditure', management.income_expenditure,
         name="income&expenditure"),
    path('yearlyincome&expenditure', management.stats_income_expenditure,
         name="yearlyincome&expenditure"),
    path('accountreceivable', management.account_receivable,
         name="accountreceivable"),
    path('manage_fees', management.manage_fees,name="manage_fees"),
    
    path('broadcast', management.broadcast, name="broadcast"),
    path('manage_sms', management.manage_sms, name="manage_sms"),
    
    path('dashboard', management.dashboard, name="dashboard"),
    path('staff_dashboard', staff.staff_dashboard, name="staff_dashboard"),
    path('principaldashboard', principal.principaldashboard,name="principaldashboard"),
    path('parentdashboard', parent.parentdashboard,name="parentdashboard"),
    
    
    path('change-password/', views.change_password, name='change_password'),
    path('reminders', management.reminders, name='reminders'),
    
    path('load_term', management.load_term, name='load_term'),
    
    
    
    path('viewing_results', staff.viewing_results, name='viewing_results'),
    path('add_resultss/<str:pk>/', staff.add_resultss, name='add_resultss'),
    path('print_student_results/<str:pk>/',
         staff.print_student_results, name='print_student_results'),
    path('view_student_results/<str:pk>/',
         staff.view_student_results, name='view_student_results'),
    
    path('child_results', parent.child_results, name='child_results'),
    
]
