import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Driver, Car


def validate_license_number(value: str):
    if not re.match(r"^[A-Z]{3}[0-9]{5}$", value):
        raise ValidationError(
            "Format: 3 Upper letters + 5 number (Example: ABC12345)"
        )


class DriverForm(forms.ModelForm):
    license_number = forms.CharField(
        max_length=8 ,
        validators=[validate_license_number],
    )

    class Meta:
        model = Driver
        fields = "__all__"


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(
        max_length=8,
        validators=[validate_license_number],
    )

    class Meta:
        model = Driver
        fields = ("license_number",)


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "drivers": forms.CheckboxSelectMultiple(),
        }
