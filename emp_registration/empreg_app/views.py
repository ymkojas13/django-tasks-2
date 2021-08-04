from .models import EmpReg
from django.shortcuts import render
from .forms import EmpForm

# Create your views here.
def empindex(request):
    emp_details = EmpReg.objects.all()
    return render(request,'empreg_app/emp.html', {'emp':emp_details})

def empindex2(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            emp_id = form.cleaned_data.get("emp_id")
            name = form.cleaned_data.get("name")
            dept = form.cleaned_data.get("dept")
            emp_save = EmpReg(emp_id = emp_id, name = name, dept = dept)
            emp_save.save()
        return render(request, 'empreg_app/emp2.html', {'form':form})
    else:
        form = EmpForm()
        return render(request, 'empreg_app/emp2.html', {'form':form})
