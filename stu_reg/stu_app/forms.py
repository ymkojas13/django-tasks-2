from django import forms

class StudentForm(forms.Form):
    stu_id = forms.IntegerField()
    name = forms.CharField(max_length=20)
    dept = forms.CharField(max_length=20)