from django.shortcuts import render, redirect
from .forms import RegistrationForm

def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})
