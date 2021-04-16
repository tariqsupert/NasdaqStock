from django import forms
from .models import Tickers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class StockForm(forms.ModelForm):
    class Meta:
        model = Tickers
        fields = ["ticker"]

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
      

    def save(self, commit=True):
        user = super ( CustomRegistrationForm, self ).save(commit=False)
                
        user.email = self.cleaned_data ['email']
        user.is_staff = True
        

        if commit :
            user.save()

        return user