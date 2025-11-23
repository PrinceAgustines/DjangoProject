from django.contrib import admin
from .models import TestingDatabase, Student, School, Enrollment, Course, TuitionPayment

admin.site.register(TestingDatabase)

admin.site.register(Student)
admin.site.register(School)
admin.site.register(Enrollment)
admin.site.register(Course)
admin.site.register(TuitionPayment)

# Register your models here.
