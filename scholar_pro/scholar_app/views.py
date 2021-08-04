from django.shortcuts import render
from .forms import ScholarModelForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ScholarModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            id = form.cleaned_data['id']
            course = form.cleaned_data['course']
            rembus = form.cleaned_data['rembursment']
        return render(request, 'index.html', {'form': form})
    else:
        form = ScholarModelForm()
        return render(request, 'index.html',{'form': form})