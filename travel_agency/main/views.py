from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from django.utils.translation import gettext as _

from .models import Contact

class HomeCreateView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'index.html'
    success_url = '/'


def set_languages(request):
    lang = request.POST.get('language')
    return redirect(f'/{lang}/')

