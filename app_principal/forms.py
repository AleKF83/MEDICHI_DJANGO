from django import forms


class LoginForm(forms.Form):
    numero_afiliado = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Número de afiliado'}))
    contrasena = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    

class AfiliarseForm(forms.Form):
    plan_select = [
        (1, "Plan 300"),
        (2, "Plan 400"),
        (3, "Plan 400"),
        (4, "Plan Platinum"), 
]   
    nombre_completo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre Completo'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    telefono = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}))
    #plan = forms.MultipleChoiceField(choices = plan_select)    
    plan = forms.ChoiceField(choices=plan_select, widget=forms.Select(attrs={'placeholder': 'Selecciona un plan'}))