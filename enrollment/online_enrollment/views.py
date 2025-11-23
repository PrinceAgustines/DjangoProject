from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import StudentForm, SchoolForm, EnrollmentForm, CourseForm, TuitionPaymentForm, StudentRegisterForm
from .models import Student, School, Enrollment, Course, TuitionPayment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.

#STUDENT
def students(request):
    # Get the search query from the request
    query = request.GET.get('search', '')  # Default to an empty string if no query is provided
    
    # Filter students based on the search query
    if query:
        studInfo = Student.objects.filter(name__icontains=query).values()  # Search by name (case-insensitive)
    else:
        studInfo = Student.objects.all().values()  # Fetch all students if no query
    
    # Render the template with the filtered student data
    return render(request, 'students.html', {'students': studInfo, 'search_query': query})

#SCHOOL
def schools(request):
    # Get the search query from the request
    query = request.GET.get('search', '')  # Default to an empty string if no query is provided
    
    # Filter schools based on the search query
    if query:
        schoolInfo = School.objects.filter(school_name__icontains=query).values()  # Search by school name (case-insensitive)
    else:
        schoolInfo = School.objects.all().values()  # Fetch all schools if no query
    
    # Render the template with the filtered school data
    return render(request, 'schools.html', {'schools': schoolInfo, 'search_query': query})

#ENROLLMENT
def enrollments(request):
    # Get the search query from the request
    query = request.GET.get('search', '')  # Default to an empty string if no query is provided
    
    # Filter enrollments based on the search query
    if query:
        enroll = Enrollment.objects.filter(student_ID__icontains=query).values()  # Search by student ID (case-insensitive)
    else:
        enroll = Enrollment.objects.all().values()  # Fetch all enrollments if no query
    
    # Render the template with the filtered enrollment data
    return render(request, 'enrollments.html', {'enrollments': enroll, 'search_query': query})

#COURSE
def course(request):
    # Get the search query from the request
    query = request.GET.get('search', '')  # Default to an empty string if no query is provided
    
    # Filter courses based on the search query
    if query:
        courseInfo = Course.objects.filter(course_name__icontains=query).values()  # Search by course name (case-insensitive)
    else:
        courseInfo = Course.objects.all().values()  # Fetch all courses if no query
    
    # Render the template with the filtered course data
    return render(request, 'courses.html', {'course': courseInfo, 'search_query': query})

#TUITION PAYMENT
def tuitionPayments(request):
    # Get the search query from the request
    query = request.GET.get('search', '')  # Default to an empty string if no query is provided
    
    # Filter tuition payments based on the search query
    if query:
        payments = TuitionPayment.objects.filter(fee_ID__icontains=query).values()  # Search by fee ID (case-insensitive)
    else:
        payments = TuitionPayment.objects.all().values()  # Fetch all payments if no query
    
    # Render the template with the filtered payment data
    return render(request, 'tuitionPayments.html', {'tuitionPayments': payments, 'search_query': query})

#Forms

def studentform_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Students')
    else:
        form = StudentForm()
    return render(request, 'studentform.html', {'form':form})

def schoolform_view(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('School')
    else:
        form = SchoolForm()
    return render(request, 'schoolform.html', {'form': form})

def enrollmentform_view(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Enrollment')  
    else:
        form = EnrollmentForm()
    return render(request, 'enrollmentform.html', {'form': form})

def courseform_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Course')
    else:
        form = CourseForm()
    return render(request, 'courseform.html', {'form': form})

def tuitionpaymentform_view(request):
    if request.method == 'POST':
        form = TuitionPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TuitionPayment')
    else:
        form = TuitionPaymentForm()
    return render(request, 'tuitionpaymentform.html', {'form': form})


#Register/Login

def register_user(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created')
            return redirect('login_user')
        else:
            messages.error(request, 'Please Correct the errors below')
    else:
        form = StudentRegisterForm()
    return render(request, 'accounts/register.html',{'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid input')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('login_user')

def dashboard(request):
    # Fetch all data
    query = request.GET.get('search', '')  # Get the search query from the request
    if query:
        studInfo = Student.objects.filter(name__icontains=query).values()  # Filter students by name
    else:
        studInfo = Student.objects.all().values()  # Fetch all students if no query
    
    # Fetch other data
    total_students = Student.objects.count()
    total_enrollments = Enrollment.objects.count()
    total_courses = Course.objects.count()
    total_payments = TuitionPayment.objects.count()
    recent_students = Student.objects.order_by('-id')[:5]

    # Pass the data to the template
    return render(request, 'dashboard.html', {
        'students': studInfo,
        'total_students': total_students,
        'total_enrollments': total_enrollments,
        'total_courses': total_courses,
        'total_payments': total_payments,
        'recent_students': recent_students,
    })










#Just for testing purpose 
def testings(request):
    # Fetch all data
    query = request.GET.get('search', '')  # Get the search query from the request
    if query:
        studInfo = Student.objects.filter(name__icontains=query).values()  # Filter students by name
    else:
        studInfo = Student.objects.all().values()  # Fetch all students if no query
    
    studInfo = Student.objects.all().values()
    schooolInfo = School.objects.all().values()
    enrollInfo = Enrollment.objects.all().values()
    courseInfo = Course.objects.all().values()
    paymentInfo = TuitionPayment.objects.all().values()
    
    # Count the total number of data
    total_students = Student.objects.count()
    total_schools = School.objects.count()
    total_enrollments = Enrollment.objects.count()
    total_courses = Course.objects.count()
    total_payments = TuitionPayment.objects.count()

    # recently added
    recent_students = Student.objects.order_by('-id')[:5]
    
    # data to the template
    return render(request, 'dashboard.html', {
        'students': studInfo,
        'schools': schooolInfo,
        'enrollments': enrollInfo,
        'courses': courseInfo,
        'payments': paymentInfo,
        #
        'total_students': total_students,
        'total_schools': total_schools,
        'total_enrollments': total_enrollments,
        'total_courses': total_courses,
        'total_payments': total_payments,
        #
        'recent_students': recent_students,
    })