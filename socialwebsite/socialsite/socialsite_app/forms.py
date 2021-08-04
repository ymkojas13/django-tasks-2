from django import forms

CHOICES = [
    ("1", "Keep Logged in"),
    ("2", "Logged Out"),
    ("3", "remind Later"),
]

CHOICES2=[('select1','Female'),
         ('select2','Male')]

class SocialSiteForm(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}),label='Enter Name', label_suffix=':')
    email = forms.EmailField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)
    comment = forms.CharField(widget=forms.Textarea)
    choice = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=CHOICES,)
    like = forms.ChoiceField(choices=CHOICES2, widget=forms.RadioSelect)
