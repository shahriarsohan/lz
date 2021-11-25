from django.shortcuts import render

# Create your views here.
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success-contact.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
