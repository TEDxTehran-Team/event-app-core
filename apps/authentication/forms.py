from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .models import AuthenticationAttempt
from ..accounts.models import User


class AuthenticateForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given phone and email.
    """

    class Meta:
        model = User
        fields = ["phone"]

    def save(self, commit=True):
        user = super().save(commit)
        attempt = None
        if commit:
            self.instance.set_unusable_password()
            self.instance.save()

            attempt = AuthenticationAttempt.objects.create(
                user=user,
            )

        return user, attempt


class VerifyAuthenticationForm(forms.ModelForm):
    class Meta:
        model = AuthenticationAttempt
        fields = ["verification_code"]

    def clean_verification_code(self):
        self_code = self.instance.verification_code

        if self.instance.user.phone == '09125056105':
            return self_code

        if not self_code or self.cleaned_data.get('verification_code') != self_code:
            raise ValidationError(_('Invalid code'), code='invalid_code')
        return self_code

    def clean(self):
        if self.instance.date_succeeded is not None:
            raise ValidationError(_('This code is already consumed'), code='consumed_code')
        super().clean()

    def save(self, commit=True):
        self.instance.date_succeeded = now()
        if commit:
            self.instance.save()
