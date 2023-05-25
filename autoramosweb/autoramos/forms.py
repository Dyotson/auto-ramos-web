from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML, Submit

class ScheduleTaskForm(forms.Form***REMOVED***:
    date = forms.DateField(input_formats=['%d/%m/%Y'***REMOVED***
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'***REMOVED***, help_text='En Formato 24hrs'***REMOVED***
    nrc1 = forms.CharField(max_length=5, help_text='Ramo 1', required=True***REMOVED***
    nrc2 = forms.CharField(max_length=5, help_text='Ramo 2', required=False***REMOVED***
    nrc3 = forms.CharField(max_length=5, help_text='Ramo 3', required=False***REMOVED***
    nrc4 = forms.CharField(max_length=5, help_text='Reemplazo ramo 1', required=False***REMOVED***
    nrc5 = forms.CharField(max_length=5, help_text='Reemplazo ramo 2', required=False***REMOVED***
    nrc6 = forms.CharField(max_length=5, help_text='Reemplazo ramo 3', required=False***REMOVED***

    def __init__(self, *args, **kwargs***REMOVED***:
        super(***REMOVED***.__init__(*args, **kwargs***REMOVED***
        self.helper = FormHelper(self***REMOVED***
        self.helper.layout = Layout(
            Row(
                Column('date'***REMOVED***,
                Column('time'***REMOVED***,
                css_class = 'row'
***REMOVED***
            HTML("<br>"***REMOVED***,
            Row(
                Column('nrc1'***REMOVED***,
                Column('nrc4'***REMOVED***, 
                css_class = 'row'
***REMOVED***
            Row(
                Column('nrc2'***REMOVED***,
                Column('nrc5'***REMOVED***,
                css_class = 'row'
***REMOVED***
            Row(
                Column('nrc3'***REMOVED***,
                Column('nrc6'***REMOVED***,
                css_class = 'row'
            ***REMOVED***
        ***REMOVED***
        self.helper.add_input(Submit('submit', 'Reservar Toma de Ramos', css_class = 'btn btn-success'***REMOVED***

class ReLogin(forms.Form***REMOVED***:
***REMOVED***word = forms.CharField(widget=forms.PasswordInput***REMOVED***
