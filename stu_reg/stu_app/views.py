from django.shortcuts import render
from .models import StudentReg
from .forms import StudentForm

# Create your views here.
def stuindex(request):
    stu_details = StudentReg.objects.all()
    return render(request,'student.html', {'stu':stu_details})

def stuindex2(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            stu_id = form.cleaned_data.get("stu_id")
            name = form.cleaned_data.get("name")
            dept = form.cleaned_data.get("dept")
            emp_save = StudentReg(stu_id = stu_id, name = name, dept = dept)
            emp_save.save()
        return render(request, 'student2.html', {'form':form})
    else:
        form = StudentForm()
        return render(request, 'student2.html', {'form':form})