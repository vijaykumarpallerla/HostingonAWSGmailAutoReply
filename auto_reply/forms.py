from django import forms

class SignatureForm(forms.Form):
    signature_html = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)
