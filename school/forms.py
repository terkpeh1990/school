from django import forms
from django.forms import Form
from django.contrib.auth import authenticate, get_user_model

import datetime
from .import models
from .models import SessionYearModel, SessionTermModel

class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.ModelForm):

    class Meta:
        model = models.Students
        exclude = ('id', 'created_at', 'updated_at', 'doc',
                   'doc_phone', 'expiled', 'expiled_detail', 'public_nurse', 'remarks', 'admin', 'stu_status','att','parent_id')

        widgets = {
            'dob': DateInput(),
        }
        labels = {
            'parent_id': 'Select Parent',
            'course_id': 'Class',
            'dob': 'Date of Birth',
            'description': 'Description',
            'preferredname': 'Preferred Name',
            'session_year_id': 'Academic year',

        }
class EditStudentForm(forms.ModelForm):

    class Meta:
        model = models.Students
        exclude = ('id', 'created_at', 'updated_at', 'doc',
                   'doc_phone', 'expiled', 'expiled_detail', 'public_nurse', 'remarks', 'admin','att','parent_id')

        widgets = {
            'dob': DateInput(),
        }
        labels = {
            'parent_id': 'Select Parent',
            'course_id': 'Class',
            'dob': 'Date of Birth',
            'description': 'Description',
            'preferredname': 'Preferred Name',
            'session_year_id': 'Academic year',
            'stu_status':'Status',

        }


class AddParentForm(forms.ModelForm):

    class Meta:
        model = models.Parents
        exclude = ('id','ftitle', 'mtitle')

        labels = {
            'father_name': "Father's/Guardian's full Name(A)",
            'mother_name': "Mother's/Guardian's full Name(B)",
            'father_tel':'Busness Tel',
            'father_phone': 'Cell Phone No.',
            'mother_tel': 'Busness Tel',
            'mother_phone': 'Cell Phone No.',
            'fsilent': 'Silent Tel. No.',
            'msilent': 'Silent Tel. No.',
            'frelationship': 'Relationship to student',
            'mrelationship': 'Relationship to student',
        }

class AddEducationForm(forms.ModelForm):
    
    class Meta:
        model = models.EducationHistory
        exclude = ('student_id',)
        
        widgets = {
            'startdate': DateInput(),
            'enddate': DateInput(),
        }

        labels = {
            'schname': "Name of School",
            'address': "Address",
            'startdate': 'Start Date',
            'enddate': 'End Date',
            'lastclass': 'Last Class', 
        }


class EmmercencyForm(forms.ModelForm):

    class Meta:
        model = models.EmmergencyContacts
        exclude = ('student_id',)

class MedicalForm(forms.ModelForm):
    
    class Meta:
        model = models.MedicalHistory
        exclude = ('student_id',)
        
        labels = {
            'condition': "Condition/Allergies",
        }
        

class DoctorForm(forms.ModelForm):

    class Meta:
        model = models.Students
        fields = ('doc', 'doc_phone', 'public_nurse',)
        
        labels = {
            'doc': "Doctor's Name",
            'public_nurse': "Consent to see public health Nurse",
            
        }
    
class ImmunizationForm(forms.ModelForm):
    
    class Meta:
        model = models.ImmunisationHistory
        exclude = ('student_id',)
        
        widgets = {
            'givendate': DateInput(),
           
        }
        
        labels = {
            'givendate': "Date given",  
        }      


class AddStaffForm(forms.ModelForm):
    
    class Meta:
        model = models.Staffs
        exclude = ('id', 'created_at', 'updated_at', 'staff_status',)

        widgets = {
            'dob': DateInput(),
        }
        labels = {
            'course_id': 'Class',
            'dob': 'Date of Birth',
            'preferredname': 'Preferred Name',
        }


class AddStaffEducationForm(forms.ModelForm):

    class Meta:
        model = models.StaffEducationHistory
        exclude = ('staff_id',)

        widgets = {
            'startdate': DateInput(),
            'enddate': DateInput(),
        }

        labels = {
            'schname': "Name of School",
            'startdate': 'Start Date',
            'enddate': 'End Date',
        }

class AddStaffWorkExperenceForm(forms.ModelForm):
    
    class Meta:
        model = models.StaffWorkExperience
        exclude = ('staff_id',)

        widgets = {
            'startdate': DateInput(),
            'enddate': DateInput(),
        }

        labels = {
            'startdate': 'Start Date',
            'enddate': 'End Date',
        }

class StaffEmmercencyForm(forms.ModelForm):
    
    class Meta:
        model = models.StaffEmmergencyContacts
        exclude = ('staff_id',)


class AcademicYearForm(forms.ModelForm):
    
    def clean(self, *args, **kwargs):
        try:
            prev_acadamic_year = SessionYearModel.objects.last()
        except SessionYearModel.DoesNotExist:
            pass
        if prev_acadamic_year:
            check = self.cleaned_data.get('session_start_year')
            if check <= prev_acadamic_year.session_end_year:
                raise forms.ValidationError({'session_start_year': ["Previous Acadamic Year is Still Running", ]})
        return super(AcademicYearForm, self).clean(*args, **kwargs)
            

    class Meta:
        model = models.SessionYearModel
        exclude = ('id',)
        
        widgets = {
            'session_start_year': DateInput(),
            'session_end_year': DateInput(),
        }
        
        labels = {
            'session_start_year': 'Start Date',
            'session_end_year': 'End Date',
        }


class EdithAcademicYearForm(forms.ModelForm):

    class Meta:
        model = models.SessionYearModel
        exclude = ('id',)

        widgets = {
            'session_start_year': DateInput(),
            'session_end_year': DateInput(),
        }

        labels = {
            'session_start_year': 'Start Date',
            'session_end_year': 'End Date',
        }
        
class AcademicTermForm(forms.ModelForm):
    
    class Meta:
        model = models.SessionTermModel
        exclude = ('id', 'acadamic_year',)
        
        widgets = {
            'term_start_date': DateInput(),
            'term_end_end': DateInput(),
        }
        
        labels = {
            'term_start_date': 'Start Date',
            'term_end_end': 'End Date',
        }
    
   


class AddClassForm(forms.ModelForm):

    class Meta:
        model = models.SchClass
        fields = ('class_name',)

        labels = {
            'class_name': 'Name Of Class',
        }
    

class AddSubjectForm(forms.ModelForm):
    
    class Meta:
        model = models.Subjects
        exclude = ('created_at', 'updated_at', 'class_id',)

        labels = {
            'class_id': 'Select Class',
        } 


class EditSubjectForm(forms.ModelForm):

    class Meta:
        model = models.Subjects
        exclude = ('created_at', 'updated_at',)

        labels = {
            'class_id': 'Select Class',
        }

class AddAttendance(forms.ModelForm):
    
    class Meta:
        model = models.Attendance
        fields = ('class_id', 'attendance_date','session_year_id', 'term_year_id',)
        
        widgets = {
            'attendance_date': DateInput(),
        }

        labels = {
            'class_id': 'Select Class',
            'session_year_id': 'Select Academic Year',
            'term_year_id': 'Select Academic Term',
        }
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['term_year_id'].queryset = SessionTermModel.objects.none()

    #     if 'session_year_id' in self.data:
    #         try:
    #             session_year_id = int(self.data.get('session_year_id'))
    #             self.fields['term_year_id'].queryset = SessionTermModel.objects.filter(session_year_id =session_year_id )
    #         except (ValueError, TypeError):
    #             pass
    #     elif self.instance.pk:
    #         self.fields['term_year_id'].queryset = self.instance.session_year_id.term_year_id_set


class TakeAttendance(forms.ModelForm):
    status = forms.BooleanField(label=False)

    class Meta:
        model = models.AttendanceReport
        fields = ('status', )


class AddResults(forms.ModelForm):

    class Meta:
        model = models.Results
        fields = ('class_id', )

        labels = {
            'class_id': 'Select Class',
        }

class AddStudentResults(forms.ModelForm):
    
    class Meta:
        model = models.StudentResult
        fields = ('subject_assignment_marks', 'subject_exam_marks', 'remarks',)

        labels = {
            'subject_assignment_marks': 'Class Score',
            'subject_exam_marks':'Exams Score',
        }

class AddPromotionForm(forms.ModelForm):
    
    class Meta:
        model = models.Students
        fields = ('course_id','remarks')

        widgets = {
            'dob': DateInput(),
        }
        labels = {
            'course_id': 'Promote To',
        }


class AddBillForm(forms.ModelForm):

    class Meta:
        model = models.Bills
        fields = ('class_id', 'bill_date', 'session_year_id', 'term_year_id',)

        widgets = {
            'bill_date': DateInput(),
        }

        labels = {
            'class_id': 'Select Class',
            'bill_date':'Date of Bill',
            'session_year_id':'Select Academic Year',
            'term_year_id': 'Select Academic Term',
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['term_year_id'].queryset = SessionTermModel.objects.none()

    #     if 'session_year_id' in self.data:
    #         try:
    #             session_year_id = int(self.data.get('session_year_id'))
    #             self.fields['term_year_id'].queryset = SessionTermModel.objects.filter(
    #                 session_year_id=session_year_id)
    #         except (ValueError, TypeError):
    #             pass
    #     elif self.instance.pk:
    #         self.fields['term_year_id'].queryset = self.instance.session_year_id.term_year_id_set

class BillClassForm(forms.ModelForm):
    
    class Meta:
        model = models.Bills_class
        fields = ('description', 'amount',)


class AddPayrollForm(forms.ModelForm):
    
    class Meta:
        model = models.Payroll
        fields = ( 'session_year_id', 'term_year_id',)

        labels = {   
            'session_year_id':'Select Academic Year',
            'term_year_id': 'Select Academic Term',
        }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['term_year_id'].queryset = SessionTermModel.objects.none()

    #     if 'session_year_id' in self.data:
    #         try:
    #             session_year_id = int(self.data.get('session_year_id'))
    #             self.fields['term_year_id'].queryset = SessionTermModel.objects.filter(
    #                 session_year_id=session_year_id)
    #         except (ValueError, TypeError):
    #             pass
    #     elif self.instance.pk:
    #         self.fields['term_year_id'].queryset = self.instance.session_year_id.term_year_id_set


class AccountCodeForm(forms.ModelForm):

    class Meta:
        model = models.Account_code
        fields = ('code', )

        labels = {
            'code': 'Account Code',
        }

class PvForm(forms.ModelForm):
    
    class Meta:
        model = models.Pv
        exclude = ('id','status', 'created_date',)


class PvDetailForm(forms.ModelForm):

    class Meta:
        model = models.Pv_details
        exclude = ('id', 'pv',)


# class paymentform(forms.ModelForm):

#     class Meta:
#         model = models.StudentBill
#         fields = ( 'amount_paid', 'paidby', 'paidbyphone',)


class paymentform(forms.Form):
    amount_paid = forms.CharField(max_length=30)
    paidby = forms.CharField(max_length=254)
    phone = forms.CharField(max_length=254)
    
class SmsForm(forms.ModelForm):
    
    class Meta:
        model = models.SMS
        fields = ('sms', )
        
        widgets = {
            
            'sms': forms.Textarea(attrs={'placeholder': 'Type a message...'}),
        }

        labels = {
            'sms': 'Message',
        }    


class UserLoginForm(forms.Form):
    username = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username or Password incorrect')
            if not user.check_password(password):
                raise forms.ValidationError('Username or Password incorrect')
            if not user.is_active:
                raise forms.ValidationError('Username or Password incorrect')
        return super(UserLoginForm, self).clean(*args, **kwargs)

    class Meta():
        model = models.User
        fields = ('username', 'password')
