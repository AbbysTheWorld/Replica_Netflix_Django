from django.shortcuts import redirect,reverse
from .models import Filme,Usuario
from .forms import CriarContaForm,FormHomePage
from django.views.generic import TemplateView,ListView,DetailView,FormView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomePage(FormView):
    template_name = 'homepage.html'
    form_class = FormHomePage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)
        
    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')

class HomeFilmes(LoginRequiredMixin,ListView):
    template_name = 'homefilmes.html'
    model = Filme

class DetalhesFilmes(LoginRequiredMixin,DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilmes,self).get_context_data(**kwargs)
        filmes_relaciondos = Filme.objects.filter(categoria=self.get_object().categoria)
        context['filmes_relaciondos'] = filmes_relaciondos

        return context
    
class PesquisaFilme(LoginRequiredMixin,ListView):
    template_name = 'pesquisahtml.html'
    model=Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('q')
        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None

class PaginaPerfil(LoginRequiredMixin,UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name','last_name','email']

    def get_success_url(self):
        return reverse('filme:homefilmes')

class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm
