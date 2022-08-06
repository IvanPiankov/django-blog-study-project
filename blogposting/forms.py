from django.core.exceptions import ValidationError
from django.forms import ModelForm

from blogposting.models import Author


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