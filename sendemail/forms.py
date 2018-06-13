from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    from_email = forms.EmailField(required=False)
    phone = forms.IntegerField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)