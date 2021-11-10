from django.urls import path

from .views import addfeedback, getReview, feedbackdetails

app_name = 'feedback'

urlpatterns = [
    path('', getReview, name='list'),
    path('add', addfeedback, name='add'),
    path('details', feedbackdetails, name='details'),
]
