from django import forms

class EmpForm(forms.Form):
    emp_id = forms.IntegerField()
    name = forms.CharField(max_length=20)
    dept = forms.CharField(max_length=20)