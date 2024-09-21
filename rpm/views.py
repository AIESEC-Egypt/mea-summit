from django.shortcuts import render, redirect
from .forms import RegistrationForm

def index(request):
    return render(request, 'index.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            registration_instance = form.save(commit=False)
            registration_instance.save()
            form.save_m2m()
            return redirect('/thankyou.html')  # Assuming you have a URL named 'thankyou'

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})

