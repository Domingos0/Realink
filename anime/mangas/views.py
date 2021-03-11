from mangas.models import Mangas
from tela.models import Sus
from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView, ListView, DeleteView, UpdateView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class Suges_admm(LoginRequiredMixin,ListView):
    model = Sus
    template_name = 'mangas/lista_adm.html'


class Excluir_susg(LoginRequiredMixin,DeleteView):
    model  = Sus
    template_name = 'mangas/susg_excluir_adm.html'
    fields = ['site_nome', 'url_nome',]
    success_url = reverse_lazy('sugestao_adm')

class ListarView(LoginRequiredMixin,ListView):
    model = Mangas
    template_name = 'mangas/listar.html'
    

class AdicionarView(LoginRequiredMixin,CreateView):
    model = Mangas
    template_name = 'mangas/adicionar.html'
    fields = ['site_nome', 'url_nome', 'nome_genero','categoria']
    success_url = reverse_lazy('listar')


class EditarView(LoginRequiredMixin,UpdateView):
    model = Mangas
    template_name = 'mangas/adicionar.html'
    fields = ['site_nome', 'url_nome', 'nome_genero','categoria']
    success_url = reverse_lazy('listar')

class ExcluirView(LoginRequiredMixin,DeleteView):
    model  = Mangas
    template_name = 'mangas/excluir.html'
    fields = ['site_nome', 'url_nome', 'nome_genero','categoria']
    success_url = reverse_lazy('listar')
