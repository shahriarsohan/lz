
from django.contrib.auth import get_user_model

from django.shortcuts import render

User = get_user_model()


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
    qs = User.objects.all()
    print(qs)
    context = {
        'qs': qs
    }

    return render(request, 'students.html', context)
