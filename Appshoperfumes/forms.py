from django import forms
from django.contrib.auth.forms import  UserChangeForm
from django.contrib.auth.models import  User
from .models import  Producto, Avatar

class ClienteFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    correo = forms.EmailField(required=True)
    direccion = forms.CharField(required=True)

#class AgregaProductoFormulario(forms.Form):

    #nombre = forms.CharField(required=True)
    #precio = forms.IntegerField(required=True)

#OTRA FORMA DE HACER EL FORMULARIO CON MODELFORM
class AgregaProductoFormulario(forms.ModelForm):

    class Meta:
        model=Producto
        fields=('__all__')


class AgregaCategoriaFormulario(forms.Form):

    nombre = forms.CharField(required=True)

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):

        print(self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
   #PARA AGREGAR EL AVATAR DESDE UN FORMULARIO DESDE LA APLICACION
class AvatarFormulario(forms.ModelForm):
    class Meta:
        model=Avatar
        fields=('imagen',)
