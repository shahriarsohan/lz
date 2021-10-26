from django.urls import path

from .views import getCourses, CourseDetailView

app_name = 'course'

urlpatterns = [
    path('', getCourses),
    path('details/<pk>', CourseDetailView.as_view(), name='details'),

]
