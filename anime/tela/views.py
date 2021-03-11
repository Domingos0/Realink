from tela.models import Sus
from mangas.models import Mangas
from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView, ListView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Tela(ListView):
    model = Mangas
    template_name = 'tela/tela_um.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['mangas'] = Mangas.objects.all().filter(categoria='manga')
    
        return context


class Tela_anime(ListView):
    model = Mangas
    template_name = 'tela/tela_dois.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['animes'] = Mangas.objects.all().filter(categoria='anime')
        
        
        return context


class Tela_novel(ListView):
    model = Mangas
    template_name = 'tela/tela_tres.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['novels'] = Mangas.objects.all().filter(categoria='novel')

        return context


class Tela_sugestao(CreateView):
    model = Sus
    success_url = reverse_lazy('manga')
    template_name = 'tela/tela_quatro.html'
    fields = ['site_nome', 'url_nome']

class Tela_cadastro(TemplateView):
    template_name = 'tela/cadastro.html'

# Create your views here.
