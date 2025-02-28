from django import forms
from .models import Book , Author
from django.contrib.auth.models import User 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =['title', 'pub_date', 'synopsis', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du livre'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Résumé'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birthday', 'biography']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du livre'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Résumé'}),
        }
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self) :
        cd = self.cleaned_data
        if cd['password'] != cd ['password2']:
            raise forms.ValidationError("Password don't match.")
        return cd['password2']