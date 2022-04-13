from random import choices
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.models import User

ROLES = (
        ('SELLER', 'SELLER'),
        ('USER', 'USER'),
        )
class LoginForm(AuthenticationForm):
    username=forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class':'form-control',
    }))
    
    
    
class UserForm(UserCreationForm):
    username=forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    email=forms.CharField(label='E-mail', widget=forms.EmailInput(attrs={
        'class':'form-control',
    }))
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class':'form-control',
    }))
    password2=forms.CharField(label='confirm your password', widget=forms.PasswordInput(attrs={
        'class':'form-control',
    }))
    contact=forms.IntegerField(label='tel', widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    
    
    
    
    

    #pour valider l'attribut ou la valeur du champ password1, on utilise la méthode clean_nomduchamp comme suit. cette methode est plus adapté lorsque on veut valider un seul champs, faire attention car ici cette methode nous fais manipuler la valeur du champs sour sa forme objet d'ou l'utilisation du self
    
    class Meta:
        model=User
        fields=('username','email','password1','password2','role','contact')