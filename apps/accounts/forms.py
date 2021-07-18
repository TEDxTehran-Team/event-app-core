from django import forms

from apps.accounts.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'job_title',
            'education_field',
            'biography',
            'interests',
        )
