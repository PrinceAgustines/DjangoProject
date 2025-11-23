from django import forms
from .models import Student, School, Enrollment, Course, TuitionPayment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_ID','name','year_level','date_of_birth','parents_contact_info']

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_ID','school_name','address','contact_number','email']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['enrollment_ID','student_ID','school_year','year_level','enrollment_status']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_ID','course_name','year_level','teacher_name','course_description']

class TuitionPaymentForm(forms.ModelForm):
    class Meta:
        model = TuitionPayment
        fields = ['fee_ID','student_ID','fee_amount','payment_status','due_date']

#REGISTER FORM

class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username','email','password1','password2']