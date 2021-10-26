from django.shortcuts import render

from course.models import Courses
from django.views.generic.detail import DetailView

# Create your views here.


def getCourses(request):
    template = 'index.html'
    courses = Courses.objects.all()
    print(courses)
    context = {"courses": courses}
    return render(request, template, context)


class CourseDetailView(DetailView):
    model = Courses
    template_name = 'details.html'
    context_object_name = 'course'
