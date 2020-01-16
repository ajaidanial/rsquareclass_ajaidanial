"""Contains all the forms for the main_app"""
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from main_app import models


class LoginForm(forms.ModelForm):
    """Form to login user"""

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]

    def clean(self):
        self._validate_unique = False
        return self.cleaned_data


class SignUpForm(forms.ModelForm):
    """Form to signup user"""

    confirm_password = forms.CharField(max_length=128)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "confirm_password",
        ]

    def clean_confirm_password(self):
        if self.cleaned_data["password"] != self.cleaned_data["confirm_password"]:
            raise ValidationError("Does not match your password.", code="invalid")
        return self.cleaned_data["confirm_password"]


class YearForm(forms.ModelForm):
    """Form for Year model"""

    class Meta:
        model = models.Year
        fields = "__all__"


class GroupForm(forms.ModelForm):
    """Form for Group model"""

    class Meta:
        model = models.Group
        fields = "__all__"


class SubjectForm(forms.ModelForm):
    """Form for Subject model"""

    class Meta:
        model = models.Subject
        fields = "__all__"


class BatchForm(forms.ModelForm):
    """Form for Batch model"""

    class Meta:
        model = models.Batch
        fields = "__all__"
