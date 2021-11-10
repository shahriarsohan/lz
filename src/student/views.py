from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from course.models import CourseContent, Courses
from cart.models import Order
from student.models import UserProfile

User = settings.AUTH_USER_MODEL


@csrf_exempt
@login_required
def paymentsuccess(request):
    orderr_qs = Order.objects.filter(user=request.user, ordered=False).first()
    if orderr_qs:
        orderr_qs.ordered = True
        orderr_qs.save()
        user_profile_qs = UserProfile.objects.filter(user=request.user).first()
        if user_profile_qs:
            print('order_qs', orderr_qs.cart.all())
            cart_qs = orderr_qs.cart.all()
            for q in cart_qs:
                print('course qs', q.course)
                user_profile_qs.courses.add(q.course)
                user_profile_qs.save()
                q.ordered = True
                q.save()
        # else:
        #     return redirect('/')
        return render(request, 'success.html')
    else:
        return render(request, 'success.html')


@login_required
def dashboard(request):
    profile_qs = UserProfile.objects.get(user=request.user)
    if profile_qs:
        courses = profile_qs.courses.all()
        context = {
            'course': courses
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/')


def detailscourse(request, pk):
    print(pk)
    course_qs = get_object_or_404(Courses, pk=pk)
    print('course_qs', course_qs)
    if course_qs:
        content_qs = CourseContent.objects.filter(course=course_qs)
        for q in content_qs:
            print('content_qsss', q.video)

        context = {
            'content': content_qs,
            'course': course_qs
        }

        return render(request, 'course-detials.html', context)
