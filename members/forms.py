from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    address= forms.CharField(max_length=120,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2','address')

    # def __init__(self,*args,**kwargs):
    #     super(RegisterUserForm,self).__init__(*args,**kwargs)

    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        #     'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
        # }
