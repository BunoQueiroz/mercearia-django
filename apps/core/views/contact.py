from django.shortcuts import render
from core.forms import ContactForms

def contact(request):
    return render(request, 'core/contact.html', context=render_form_contact())

def render_form_contact():
    contact = ContactForms()
    context = {
        'form': contact
    }
    return context
