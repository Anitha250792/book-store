from django import forms
from .data import ENQUIRY_TOPICS


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your full name",
        }),
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "+91 98765 43210",
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "you@example.com",
        }),
    )
    interested_in = forms.ChoiceField(
        choices=ENQUIRY_TOPICS,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Tell us what you're looking for...",
            "rows": 4,
        }),
    )

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        digits = "".join(ch for ch in phone if ch.isdigit())
        if len(digits) < 10:
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone
