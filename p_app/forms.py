from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class loginform(AuthenticationForm):
    username = forms.CharField(
        label="USERNAME",
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label="PASSWORD",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

class staffdataform(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = staffdata
        fields = ['staff_id', 'name', 'gender', 'phoneno', 'photo']


class bedequipform(forms.ModelForm):
    class Meta:
        model = bedequip
        fields = '__all__'


class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['feedback']  


class reportform(forms.ModelForm):
    class Meta:
        model = report
        fields = ['file', 'date']


class medicinedataform(forms.ModelForm):
    class Meta:
        model = medicinedata
        fields = ['name', 'description']


class patientdataform(forms.ModelForm):
    class Meta:
        model = patientdata
        fields = [
            'name', 'email', 'dob', 'gender', 'phoneno',
            'photo', 'place', 'district', 'state', 'pin'
        ]
