from django import forms
from .forms import InsuranceForm
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            fn = form.cleaned_data['first_name']
            ln = form.cleaned_data['last_name']
            id = form.cleaned_data['id']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
        return render(request, 'index.html', {'form':form})
    else:
        form = InsuranceForm()
        return render(request, 'index.html', {'form':form})