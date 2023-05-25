from django.shortcuts import render
from .forms import SignUpForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def register(response***REMOVED***:
    if response.method == 'POST':
        form = SignUpForm(response.POST***REMOVED***
        if form.is_valid(***REMOVED***:
            form.save(***REMOVED***
            return HttpResponseRedirect(reverse('login'***REMOVED***
    ***REMOVED***
        form = SignUpForm(***REMOVED***
    return render(response, 'register/register.html', {'form': form***REMOVED***
