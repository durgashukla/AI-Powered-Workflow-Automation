
from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry

        fields = [
            'customer_name',
            'phone_number',
            'email',
            'message',
        ]

        widgets = {
            'customer_name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name'
            }),

            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address'
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Describe your project requirements',
                'rows': 5
            }),
        }


class SuggestedResponseForm(forms.ModelForm):

    class Meta:
        model = Enquiry

        fields = ['suggested_response']

        widgets = {
            'suggested_response': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Edit AI suggested response here'
            })
        }
