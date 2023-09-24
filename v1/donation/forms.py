from .models import Donation
from django import forms
from v1.user.models import User

class DonationCreateForm(forms.ModelForm):
    donated_by = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Email Address of the donor if account exists'}))

    class Meta:
        model = Donation
        fields = ['display_name', 'item', 'no_of_item']

    def clean_donated_by(self):
        donated_by = self.cleaned_data['donated_by']
        print(donated_by)
        if donated_by != "":
            if not User.objects.filter(email=donated_by).exists():
                raise forms.ValidationError("User with that email 404")
        return donated_by
