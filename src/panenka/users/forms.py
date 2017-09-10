from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name_1',
            'last_name_2',
            'country',
            'birth_date',
        ]