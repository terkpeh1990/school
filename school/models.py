from django.contrib.auth.models import AbstractUser, User
from django_resized import ResizedImageField
from django.db import models 
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.sessions.models import Session
import datetime
from .utils import incrementor

User = settings.AUTH_USER_MODEL

class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_principal = models.BooleanField(default=False)
    is_director = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_account = models.BooleanField(default=False)
    is_bank = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class SessionYearModel(models.Model):
    ans = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    status = models.CharField(
        max_length=20, choices=ans, blank=True, null=True)
    
    
    def __str__(self):
        return self.name


class SessionTermModel(models.Model):
    ans = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    term_start_date = models.DateField()
    term_end_end = models.DateField()
    acadamic_year = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=ans, blank=True, null=True)
    

    def __str__(self):
        return self.name 


# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(models.Model):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(
        default=1, choices=user_type_data, max_length=10)
    is_new = models.BooleanField(default=False)


class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






class SchClass(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.class_name


class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    class_id = models.ForeignKey(SchClass, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


class Parents(models.Model):
    rel = (
        ('Parent', 'Parent'),
        ('Foster Parent', 'Foster Parent'),
        ('Friend', 'Friend'),
        ('Step-Parent', 'Step-Parent'),
        ('Host Family', 'Host Family'),
        ('Self', 'Self'),
        ('Adoptive Parent', 'Relative'),
        ('Other', 'Other'),
    )
    priv = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    id = models.CharField(max_length=2000, primary_key=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    ftitle = models.CharField(max_length=100, blank=True, null=True)
    father_occupation = models.CharField(max_length=255, blank=True, null=True)
    father_tel = models.CharField(max_length=20, blank=True, null=True)
    father_phone = models.CharField(max_length=20, blank=True, null=True)
    fsilent = models.CharField(max_length=20,choices=priv)
    frelationship = models.CharField(choices=rel, max_length=50)
    father_email = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)
    mtitle = models.CharField(max_length=100, blank=True, null=True)
    mother_occupation = models.CharField(max_length=255, blank=True, null=True)
    mother_tel = models.CharField(max_length=20, blank=True, null=True)
    mother_phone = models.CharField(max_length=20, blank=True, null=True)
    mother_email = models.CharField(max_length=100, blank=True, null=True)
    msilent = models.CharField(max_length=20,choices=priv)
    mrelationship = models.CharField(choices=rel, max_length=50)
    
    def __str__(self):
        return self.id
        
    def save(self):

        if not self.id:
            number = incrementor()
            self.id = "PA" + str(number())
            while Parents.objects.filter(id=self.id).exists():
                self.id = "PA" + str(number())
        super(Parents, self).save()


class Students(models.Model):
    sex = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    ans = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    stat = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    live = (
        ('Always', 'Always'),
        ('Mostly', 'Mostly'),
        ('Balance', 'Balance'),
        ('Occational', 'Occationally'),
        ('Never', 'Never'),
    )
    id = models.CharField(max_length=2000, primary_key=True)
    Surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    preferredname = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=7, choices=sex)
    place_of_birth = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100)
    residential_address = models.CharField(max_length=500)
    suburb = models.CharField(max_length=200, blank=True, null=True)
    postal_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    course_id = models.ForeignKey(SchClass, on_delete=models.DO_NOTHING,  blank=True, null=True)
    home_lanuage = models.CharField(max_length=250)
    educated_language = models.CharField(max_length=250)
    profile_pic = ResizedImageField(size=[128, 128],blank=True, null=True)
    session_year_id = models.ForeignKey(
        SessionYearModel, on_delete=models.CASCADE, blank=True, null=True)
    parent_id = models.ForeignKey(Parents, on_delete=models.CASCADE)
    admin = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    lives_with_primary_family = models.CharField(choices=live, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doc = models.CharField(max_length=225, blank=True, null=True)
    doc_phone = models.CharField(max_length=15, blank=True, null=True)
    expiled = models.CharField(
        choices=ans, max_length=5, blank=True, null=True)
    expiled_detail = models.CharField(max_length=255, blank=True, null=True)
    public_nurse = models.CharField(
        choices=ans, max_length=5, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    att = models.BooleanField(  null=True, blank=True, default=False)
    stu_status =  models.CharField(max_length=20, choices=stat)
    stu_check = models.BooleanField(default=False)
    
    def __str__(self):
        return self.id
   
    
    __original_course_id = None

    def __init__(self, *args, **kwargs):
        super(Students, self).__init__(*args, **kwargs)
        self.__original_course = self.course_id

    def save(self, force_insert=False, force_update=False, *args, **kwargs):

        if not self.id:
            number = incrementor()
            self.id = "MSAC" + str(number())
            while Students.objects.filter(id=self.id).exists():
                self.id = "MSAC" + str(number())
        
        if self.course_id != self.__original_course:
            acardyear = SessionYearModel.objects.get(status="Active")
            acardterm = SessionTermModel.objects.get(status="Active")
            cla = SchClass.objects.get(class_name=self.__original_course)
            par = Parents.objects.get(id=self.parent_id)
            res = Results.objects.get(
                session_year_id=acardyear, term_year_id=acardterm, class_id=self.__original_course)
            studenthistory.objects.create(studid=self.id,Surname=self.Surname, firstname=self.firstname, middlename=self.middlename,course_id = cla,acadamic_year= acardyear, acadamic_term= acardterm ,results=res , parent_id=par)
        super(Students, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_course = self.course_id


class Staffs(models.Model):
    stat = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    sex = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    id = models.CharField(max_length=2000, primary_key=True)
    Surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    preferredname = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=7, choices=sex)
    place_of_birth = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100)
    residential_address = models.CharField(max_length=500)
    suburb = models.CharField(max_length=200, blank=True, null=True)
    postal_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    profile_pic = ResizedImageField(size=[128, 128], blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    staff_status = models.CharField(max_length=30, choices=stat)
    course_id = models.ForeignKey(
        SchClass, on_delete=models.DO_NOTHING,  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    
    def __str__(self):
        return self.id + " " + "-" + self.firstname + " " + "-" + self.Surname
    
    def save(self):
    
        if not self.id:
            number = incrementor()
            self.id = "STF" + str(number())
            while Staffs.objects.filter(id=self.id).exists():
                self.id = "STF" + str(number())
        super(Staffs, self).save()


class StaffEducationHistory(models.Model):
    schname = models.CharField(max_length=255, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    staff_id = models.ForeignKey(
        Staffs, on_delete=models.CASCADE, blank=True, null=True)
   

class EducationHistory(models.Model):
    schname = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    lastclass = models.CharField(max_length=100, blank=True, null=True)
    student_id = models.ForeignKey(
        Students, on_delete=models.CASCADE, blank=True, null=True)
   


class EmmergencyContacts(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    student_id = models.ForeignKey(
        Students, on_delete=models.CASCADE, blank=True, null=True)
  


class StaffEmmergencyContacts(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    staff_id = models.ForeignKey(
        Staffs, on_delete=models.CASCADE, blank=True, null=True)
   


class StaffWorkExperience(models.Model):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    staff_id = models.ForeignKey(
        Staffs, on_delete=models.CASCADE, blank=True, null=True)
   


class MedicalHistory(models.Model):
    condition = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.ForeignKey(
        Students, on_delete=models.CASCADE, blank=True, null=True)
   

class ImmunisationHistory(models.Model):
    age = models.CharField(max_length=5, blank=True, null=True)
    immunisation = models.CharField(max_length=255, blank=True, null=True)
    givendate = models.DateField(blank=True, null=True)
    student_id = models.ForeignKey(
        Students, on_delete=models.CASCADE, blank=True, null=True)
  


class Attendance(models.Model):
    # class Attendance
    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(SchClass, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    session_year_id = models.ForeignKey(
        SessionYearModel, on_delete=models.CASCADE)
    term_year_id = models.ForeignKey(
        SessionTermModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return str(self.id)
    
    class Meta:
        unique_together = ('class_id', 'attendance_date',)


class AttendanceReport(models.Model):
    # Individual Student Attendance
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    
    def __str__(self):
        return str(self.id)


class LeaveReportStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   


class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   


class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 


class FeedBackStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 

class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


class NotificationStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    stafff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   


class Results(models.Model):
    # class Attendance
    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(SchClass, on_delete=models.DO_NOTHING)
    results_date = models.DateField()
    session_year_id = models.ForeignKey(
        SessionYearModel, on_delete=models.CASCADE)
    term_year_id = models.ForeignKey(
        SessionTermModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('class_id', 'results_date',)


class StudentResult(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    results_id = models.ForeignKey(Results, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    session_year_id = models.ForeignKey(
        SessionYearModel, on_delete=models.CASCADE, null=True,blank=True)
    term_year_id = models.ForeignKey(
        SessionTermModel, on_delete=models.CASCADE, null=True, blank=True)
    course_id = models.ForeignKey(SchClass, on_delete=models.DO_NOTHING,  blank=True, null=True)
    subject_exam_marks = models.FloatField(default=0)
    subject_assignment_marks = models.FloatField(default=0)
    
    total = models.FloatField(default=0)
    remarks = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def save(self):
        self.total = self.subject_assignment_marks + self.subject_exam_marks
        super(StudentResult, self).save()
    
    def ranking(self):
        aggregate = StudentResult.objects.filter(
            total__gt=self.total).aggregate(ranking=Count('total'))
        return aggregate['ranking'] + 1

class studenthistory(models.Model):
    id = models.AutoField(primary_key=True)
    studid = models.CharField(max_length=2000)
    Surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    course_id = models.ForeignKey(SchClass, on_delete=models.DO_NOTHING,  blank=True, null=True)
    acadamic_year = models.ForeignKey(
        SessionYearModel, on_delete=models.DO_NOTHING,  blank=True, null=True)
    acadamic_term = models.ForeignKey(
        SessionTermModel, on_delete=models.DO_NOTHING,  blank=True, null=True)
    results =models.ForeignKey(Results, on_delete=models.DO_NOTHING, blank=True, null=True)
    parent_id = models.ForeignKey(
        Parents, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        unique_together = ('studid', 'results',)

class Bills(models.Model):
    # class Attendance
    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(SchClass, on_delete=models.DO_NOTHING)
    bill_date = models.DateField()
    session_year_id = models.ForeignKey(
        SessionYearModel, on_delete=models.CASCADE)
    term_year_id = models.ForeignKey(
        SessionTermModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('class_id', 'bill_date',)


class Bills_class(models.Model):
    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(SchClass, on_delete=models.DO_NOTHING)
    bill_id = models.ForeignKey(
        Bills, on_delete=models.CASCADE)
    bill_date = models.DateField(auto_now_add=True)
    session_year_id = models.ForeignKey(
        SessionYearModel, on_delete=models.CASCADE)
    term_year_id = models.ForeignKey(
        SessionTermModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.id)
    
    class Meta:
        unique_together = ('bill_id', 'description',)


class StudentBill(models.Model): 
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(
        Students, on_delete=models.DO_NOTHING, null=True, blank=True)
    session_year_id = models.ForeignKey(
        SessionYearModel, on_delete=models.CASCADE, null=True, blank=True)
    term_year_id = models.ForeignKey(SessionTermModel, on_delete=models.CASCADE,null=True,blank=True)
    bill_id = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paidby = models.CharField(max_length=255,null=True,blank=True)
    paidbyphone = models.CharField(max_length=255, null=True, blank=True)
    bill_date = models.DateField(auto_now_add=True)
    parent_id = models.CharField(max_length=255, null=True, blank=True)
    
   
    

class Account_code(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    
    def __str__(self):
        return self.code
    
class Pv(models.Model):
    sts= (
        ('pending','pending'),
        ('approved','approved'),
        ('cancelled','cancelled'),
    )
    id = models.CharField(max_length=100, primary_key=True)
    account_code = models.ForeignKey(Account_code, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices= sts)
    created_date = models.DateField(auto_now_add=True)
  
    def save(self, *args, **kwargs):
        if not self.id:
            number = incrementor()
            self.id = "PV" + str(number())
            while Pv.objects.filter(id=self.id).exists():
                self.id = "PV" + str(number())
        super(Pv, self).save(*args, **kwargs)


class Pv_details(models.Model):
    id = models.AutoField(primary_key=True)
    pv = models.ForeignKey(Pv, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Revenue(models.Model):
   
    id = models.CharField(max_length=100, primary_key=True)
    account_code = models.ForeignKey(Account_code, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stubill = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.account_code + " " + str(self.amount)

    def save(self, *args, **kwargs):
        

        if not self.id:
            number = incrementor()
            self.id = "REV" + str(number())
            while Revenue.objects.filter(id=self.id).exists():
                self.id = "REV" + str(number())
        super(Revenue, self).save(*args, **kwargs)


class Expenditure(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    account_code = models.ForeignKey(Account_code, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_date = models.DateField(auto_now_add=True)
    pvno = models.ForeignKey(Pv, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_code + " " + str(self.amount)

    def save(self, *args, **kwargs):
        

        if not self.id:
            number = incrementor()
            self.id = "EXP" + str(number())
            while Expenditure.objects.filter(id=self.id).exists():
                self.id = "EXP" + str(number())
        super(Expenditure, self).save(*args, **kwargs)


class Payroll(models.Model):
    id = models.AutoField(primary_key=True)
    payroll_date = models.DateField(auto_now_add=True,)
    session_year_id = models.ForeignKey(
        SessionYearModel, on_delete=models.CASCADE, null=True, blank=True)
    term_year_id = models.ForeignKey(
        SessionTermModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.account_code + " " + str(self.amount)

class SMS(models.Model):
    sms_date = models.DateTimeField(auto_now_add=True)  
    sms = models.CharField(max_length=255)  
    
    def __str__(self):
        return self.sms
