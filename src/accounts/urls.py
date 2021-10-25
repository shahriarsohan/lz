from django.urls import path

from .views import signup


app_name = 'accounts'

urlpatterns = [
    path('registration', signup, name='user_sign_up')
]
