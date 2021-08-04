from .forms import SocialSiteForm
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SocialSiteForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Username']
            password = form.cleaned_data['password']
            comment = form.cleaned_data['comment']
            email = form.cleaned_data['email']
        return render(request, 'index.html', {'form':form})
    else:
        form = SocialSiteForm()
        return render(request, 'index.html', {'form':form})