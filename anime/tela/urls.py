from django.urls import path
from .views import Tela, Tela_anime, Tela_novel, Tela_sugestao, Tela_cadastro

urlpatterns = [
    path('manga/', Tela.as_view(),name='manga'),
    path('anime/', Tela_anime.as_view(),name='anime'),
    path('novel/', Tela_novel.as_view(),name='novel'),
    path('sugestão/', Tela_sugestao.as_view(),name='sugestão'),
    path('cadastro/', Tela_cadastro.as_view(),name='cadastro'),


]