from django import forms

class MemeForm(forms.Form):
    top_text = forms.CharField(max_length=100, required=True)
    bottom_text = forms.CharField(max_length=100, required=True)
    image = forms.ImageField(required=True)