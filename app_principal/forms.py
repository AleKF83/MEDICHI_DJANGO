from django import forms


class LoginForm(forms.Form):
    numero_afiliado = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Número de afiliado'}),required=True)
    contrasena = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}), required=True)

    

class AfiliarseForm(forms.Form):
    plan_select = [
        (1, "Plan 300"),
        (2, "Plan 400"),
        (3, "Plan 400"),
        (4, "Plan Platinum"), 
]   
    nombre_completo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre Completo'}), required= True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required= True)
    telefono = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}), required=True)
    #plan = forms.MultipleChoiceField(choices = plan_select)    
    plan = forms.ChoiceField(choices=plan_select, widget=forms.Select(attrs={'placeholder': 'Selecciona un plan'}), required=True)
    
class LoginMedico(forms.Form):
    matricula = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Matrícula'}),required=True)
    contrasena = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}), required=True)