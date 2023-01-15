from  django.shortcuts import redirect, render
from core.forms import ContactForms

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/index.html', context=render_form_contact())

def render_form_contact():
    contact = ContactForms()
    context = {
        'form': contact
    }
    return context
