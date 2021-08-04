from django.shortcuts import render
from .models import regmode
from .form import rforms

# Create your views here.

def Showinformation(request):

    if request.method=='POST':
        fm = rforms(request.POST)
        if fm.is_valid():
            fn=fm.cleaned_data['fname']
            ln = fm.cleaned_data['lname']
            em = fm.cleaned_data['email']
            con = fm.cleaned_data['contact']
            pa = fm.cleaned_data['password']
            conp = fm.cleaned_data['conpassword']
            regf=regmode(fname=fn,lname=ln,email=em,contact=con,password=pa,conpassword=conp)
            regf.save()
    else:
        fm = rforms()
    return render(request, 'reghtml.html', {'reght': fm})


