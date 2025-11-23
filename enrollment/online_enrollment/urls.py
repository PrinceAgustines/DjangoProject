from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('student/', views.students, name='Students'),
    path('student/add/', views.studentform_view, name='AddStudent'),
    ####
    path('school/', views.schools, name='School'),
    path('school/add/', views.schoolform_view, name='AddSchool'),
    ####
    path('enrollment/', views.enrollments, name='Enrollment'),
    path('enrollment/add/', views.enrollmentform_view, name='AddEnrollment'),
    ####
    path('course/', views.course, name='Course'),
    path('course/add/', views.courseform_view, name='AddCourse'),
    ####
    path('tuitionPayment/', views.tuitionPayments, name='TuitionPayment'),
    path('tuitionPayment/add/', views.tuitionpaymentform_view, name='AddTuitionPayment'),
    ####
    path('studentform/', views.studentform_view, name='Studentform'),
    ####
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('dashboard/', views.dashboard, name='dashboard'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)