from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import widgets
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


# user registration form 
class RegistrationForm(UserCreationForm):
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="Enter the same password as before, for verification.",
        validators=[alphanumeric]
    )

    # also add some validations here 
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        fields_required = ['username', 'first_name', 'password1', 'password2']
