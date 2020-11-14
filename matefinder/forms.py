from django.forms import ModelForm
from .models import DormInformation
from django import forms


# class DormInformationForm(ModelForm):
#     class Meta:
#         model = DormInformation
#         fields = '__all__'

class DormInformationForm(forms.Form):
    name_dorm = forms.CharField(label='name_dorm', max_length=255)
    details_dorm = forms.CharField(label='details_dorm', max_length=255)
    type_dorm = forms.CharField(label='type_dorm', max_length=255)
    price = forms.IntegerField(label='price')