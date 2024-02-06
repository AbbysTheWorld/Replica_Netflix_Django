from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[:]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        return {}
    return {'lista_filmes_recentes':lista_filmes,'filme_destaque':filme_destaque}

def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[:]
    return {'lista_filmes_emalta':lista_filmes}