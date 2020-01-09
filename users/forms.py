from django import forms
from . models import User, SignupOtp


class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'password')

    def save(self, commit=True):
        user = User.objects.create_user(
            first_name=self.cleaned_data.get("first_name"),
            last_name=self.cleaned_data.get("last_name"),
            email=self.cleaned_data.get("email"),
            phone=self.cleaned_data.get("phone"),
            password=self.cleaned_data.get("password"),
        )
        return user


class SignInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')
