from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect

from course.models import Courses
from .models import FeedBack


def addfeedback(request):
    if request.method == 'POST':
        course_id = request.POST.get("course_id")
        feedback = request.POST.get("feedback")
        user = request.user
        print('id', course_id)
        print('feedback', feedback)
        course = get_object_or_404(Courses, pk=course_id)
        print(course)
        print(request.path_info)
        FeedBack.objects.create(
            user=user,
            course=course,
            feedback=feedback
        )
        return render(request, 'review-success.html')


def getReview(request):
    course_qs = Courses.objects.all()
    context = {
        'course_qs': course_qs
    }
    return render(request, 'feedback.html', context)


def feedbackdetails(request):
    query = request.GET.get('course', None)
    print('querrrrrrrrrrrrrrrrrrrrrrrrrrrry', query)
    course_qs = get_object_or_404(Courses, pk=query)
    feedaback_qs = FeedBack.objects.filter(course=course_qs)
    print('feedaback_qs', feedaback_qs)

    context = {
        'feedaback_qs': feedaback_qs
    }
    return render(request, 'feedback-list.html', context)
