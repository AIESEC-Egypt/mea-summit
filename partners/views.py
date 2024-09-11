from django.shortcuts import render, redirect
from .forms import PartnerForm

def partners(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partners')  # Redirect after POST to avoid re-submission
    else:
        form = PartnerForm()

    return render(request, 'partner.html', {'form': form})
