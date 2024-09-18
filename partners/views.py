from django.shortcuts import render, redirect
from .forms import PartnerForm

def partners(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            partners_instance = form.save(commit=False)
            partners_instance.save()
            form.save_m2m()
    else:
        form = PartnerForm()

    return render(request, 'partner.html', {'form': form})
