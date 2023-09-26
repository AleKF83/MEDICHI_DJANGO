from django import forms

class LoginForm(forms.Form):
    afiliado = forms.CharField(label="Número de afiliado:", required=True, max_length=20)
    #, initial='afiliado')
    #css class="fas fa-id-card icon",
    psw = forms.CharField (label="Contraseña", required=True, max_length=10)
