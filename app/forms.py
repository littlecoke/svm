from django import forms


class ApiForm(forms.Form):
    key = forms.CharField(max_length=255,required=True)