
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import User

class UserForm(UserCreationForm):
    #captcha = CaptchaField()
    #captcha = ReCaptchaField(widget = ReCaptchaV2Invisible)
    email = forms.EmailField(label=_('Email'), max_length=50 , help_text=_('Required when resetting password!'))
    first_name = forms.CharField(label=_('First Name'), max_length=30, required=True)
    last_name = forms.CharField(label=_('Last Name'), max_length=30, required=True)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.fields['password1'].label = _("Password")
        self.fields['password2'].label = _("Confirm Password")

    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'gender', 'phone', 'bio', 'profile_pic']
    
    def clean_username(self):
        username = self.cleaned_data['username']
        print(username)
        if username in settings.BLACKLISTED_USERNAMES:
            raise forms.ValidationError("You cannot set that username sad :P ")
        return username
