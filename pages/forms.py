from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label="Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your name",
        }),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "you@example.com",
        }),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 5,
            "placeholder": "How can I help?",
        }),
    )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
