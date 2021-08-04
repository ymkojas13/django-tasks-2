from django import forms
from django.forms import fields
from .models import Scholar

class ScholarModelForm(forms.ModelForm):
    class Meta:
        model = Scholar
        fields = ['name', 'scholar_id', 'course', 'rembursment','address','id_doc']