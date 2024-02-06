from django.urls import path,reverse_lazy
from .views import HomePage,HomeFilmes,DetalhesFilmes,PesquisaFilme,PaginaPerfil,CriarConta
from django.contrib.auth import views as auth_view

app_name = 'filme'

urlpatterns = [
    path('', HomePage.as_view(),name='homepage'),
    path('filmes/', HomeFilmes.as_view(),name='homefilmes'),
    path('filmes/<int:pk>', DetalhesFilmes.as_view(),name='detalhesfilmes'),
    path('pesquisa/',PesquisaFilme.as_view(),name='pesquisafilme'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('editarperfil/<int:pk>',PaginaPerfil.as_view(),name='editarperfil'),
    path('criarconta/',CriarConta.as_view(),name='criarconta'),
    path('mudarsenha/',auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',success_url=reverse_lazy('filme:homefilmes')),name='mudarsenha'),
    
]
