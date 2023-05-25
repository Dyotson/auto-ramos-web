***REMOVED***
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from autoramos.backend import verificar_sesion


def read_csv(path, column***REMOVED***:
    with open(path, 'r', encoding='utf-8'***REMOVED*** as f:
        reader = (line.split(','***REMOVED*** for line in f.readlines(***REMOVED***
        for line in reader:
            yield line[column***REMOVED***

class SignUpForm(UserCreationForm***REMOVED***:
    email = forms.EmailField(***REMOVED***

    def clean(self***REMOVED***:
        username = self.cleaned_data['username'***REMOVED***
    ***REMOVED***word = self.cleaned_data['password1'***REMOVED***

        if not verificar_sesion(username, password***REMOVED***:
            self.add_error('username', 'Credenciales invalidas (Recuerda ingresar tus credenciales UC***REMOVED***'***REMOVED***
            self.add_error('password1', 'Credenciales invalidas (Recuerda ingresar tus credenciales UC***REMOVED***'***REMOVED***

    def clean_username(self***REMOVED***:
        username = self.cleaned_data['username'***REMOVED***
        if User.objects.exclude(pk=self.instance.pk***REMOVED***.filter(username=username***REMOVED***.exists(***REMOVED***:
            self.add_error('username', 'Ya existe un usuario con ese nombre'***REMOVED***
        return username
    
    ***REMOVED***Whitelist***REMOVED***
    # def clean_email(self***REMOVED***:
    #     mail = self.cleaned_data['email'***REMOVED***
    #     whitelist = read_csv(os.path.join('static', 'assets', 'data', 'reserva.csv'***REMOVED***, 1***REMOVED***

    #     if mail not in whitelist:
    #         self.add_error('email', 'No estas en la lista de reservas | Utiliza el correo que ingresaste al reservar cupo.'***REMOVED***
    #     return mail

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'***REMOVED***
