
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import *
# Create your views here.


# def signup(request):
#     return render(request, 'signup.html')


def signup(request):
    if request.method == 'POST':
        form = MyCustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_login')
    else:
        form = MyCustomSignupForm()
    return render(request, 'account/signup.html', {'form': form})
