from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def instructors(request):
    return render(request, 'instructor.html')


def allcourses(request):
    return render(request, 'all-courses.html')


def feedback(request):
    return render(request, 'feedback.html')


def about(request):
    return render(request, 'about.html')


def students(request):
    return render(request, 'students.html')
