from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from blogposting.models import Author
from blogposting.tasks import send_feedback_email


class AuthorForms(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

    # validator for bio filed

    def clean_bio(self):
        bio = self.cleaned_data['bio']
        if not bio[0].isupper():
            raise ValidationError("Please start with upper symbol")
        return bio


class SendEmailForms(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={'rows': 5})
    )

    def send_email(self):
        send_feedback_email.delay(
            self.cleaned_data['email'], self.cleaned_data['message']
        )