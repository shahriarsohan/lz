from django.urls import path

from .views import getCourses, allCourses, CourseDetailView

app_name = 'course'

urlpatterns = [
    path('', getCourses),
    path('allcourses', allCourses),
    path('details/<pk>', CourseDetailView.as_view(), name='details'),

]
