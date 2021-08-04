from django import forms
class rforms(forms.Form):
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=50)
    email=forms.EmailField()
    contact=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput,max_length=50)
    conpassword=forms.CharField(widget=forms.PasswordInput,max_length=50)