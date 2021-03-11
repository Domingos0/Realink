from django.shortcuts import render
from django.views.generic import (TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = 'home/index.html'



def sair(request):
    logout(request)
    return redirect('login') 