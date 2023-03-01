from django import forms
from .models import UserFrom


class DataForm(forms.ModelForm):
    name = forms.CharField(max_length=150, required=True, label='Name',
                           widget=forms.TextInput(attrs={'class': 'form-control'})
                           )

    email = forms.CharField(max_length=100, required=True, label='Email',
                            widget=forms.EmailInput(attrs={'class': 'form-control'})
                            )

    subject = forms.CharField(max_length=50, required=True, label='Subject',
                              widget=forms.TextInput(attrs={'class': 'form-control'})
                              )

    message = forms.CharField(max_length=250, required=True, label='Message',
                              widget=forms.Textarea(attrs={'class': 'form-control'})
                              )

    class Meta:
        model = UserFrom
        fields = ['name', 'email', 'subject', 'message']
