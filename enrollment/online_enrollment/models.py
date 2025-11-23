from django.db import models

class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"
    
class Student(models.Model):
    student_ID = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    year_level = models.CharField(max_length=8)
    date_of_birth = models.DateField()
    parents_contact_info = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student_ID}"
    
class School(models.Model):
    school_ID = models.CharField(max_length=5)
    school_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.school_ID}"
    
class Enrollment(models.Model):
    enrollment_ID = models.CharField(max_length=5)
    student_ID = models.CharField(max_length=10)
    school_year = models.CharField(max_length=10)
    year_level = models.CharField(max_length=8)
    enrollment_status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.enrollment_ID}"
    
class Course(models.Model):
    course_ID = models.CharField(max_length=5)
    course_name = models.CharField(max_length=4)
    year_level = models.CharField(max_length=8)
    teacher_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_ID}"
    
class TuitionPayment(models.Model):
    fee_ID = models.CharField(max_length=5)
    student_ID = models.CharField(max_length=10)
    fee_amount = models.IntegerField()
    payment_status = models.CharField(max_length=10)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.fee_ID}"
    