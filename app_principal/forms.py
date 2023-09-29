from django import forms

from django import forms

class LoginForm(forms.Form):
    numero_afiliado = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Número de afiliado'}))
    contrasena = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
