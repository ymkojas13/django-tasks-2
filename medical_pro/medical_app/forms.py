from django import forms

CHOICES2=[('select1','Female'),
         ('select2','Male')]

class InsuranceForm(forms.Form):
    url = forms.URLField(initial='http://')
    first_name = forms.CharField(error_messages={'required': 'Please enter your First name'},label='Enter First Name', label_suffix=':')
    last_name = forms.CharField(error_messages={'required': 'Please enter your Last name'},label='Enter Last Name', label_suffix=':')
    id = forms.IntegerField(error_messages={'required': 'Please enter your Medical Insurance No'},label='Enter Insurance No.',max_value=12)
    email = forms.EmailField(error_messages={'required': 'Please enter your Email id'},max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)
    phone = forms.IntegerField(max_value=20)
    like = forms.ChoiceField(choices=CHOICES2, widget=forms.RadioSelect)
    address = forms.CharField(widget=forms.Textarea)
    time = forms.DateTimeField()

    def clean(self):
        cleaned_data= super().clean()
        valpwd=cleaned_data['password']
        valrpwd=cleaned_data['password']
        if valpwd!= valrpwd:
            raise forms.ValidationError('Password Not Matched')
