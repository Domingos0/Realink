from django.urls import path
from .views import ListarView, AdicionarView, EditarView, ExcluirView, Suges_admm, Excluir_susg

urlpatterns = [
    path('listar/', ListarView.as_view(),name='listar'),
    path('adicionar/', AdicionarView.as_view(),name='adicionar'),
    path('editar/<int:pk>', EditarView.as_view(),name='editar'),
    path('excluir/<int:pk>', ExcluirView.as_view(),name='excluir'),
    path('sugestao_adm/', Suges_admm.as_view(),name='sugestao_adm'),
    path('e/exluir_susg/<int:pk>', Excluir_susg.as_view(),name='excluir_susg'),



]