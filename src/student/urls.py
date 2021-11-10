from django.urls import path

from .views import paymentsuccess, dashboard, detailscourse

app_name = 'user'

urlpatterns = [
    path('success', paymentsuccess, name='success'),
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard/course/<pk>/details', detailscourse, name='course-details')
]
