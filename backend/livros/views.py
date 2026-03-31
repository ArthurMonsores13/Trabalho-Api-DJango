from django.http import JsonResponse
from .models import Livro

def mostrar_livros(request, genero=None):
    if not genero:
        genero = request.GET.get('genero')

    if genero:
        livros = Livro.objects.filter(genero__iexact=genero).values()
    else:
        livros = Livro.objects.all().values()
        
    if not livros.exists():
        return JsonResponse({
            "mensagem": "Nenhum livro encontrado"
        }, status=404)

    return JsonResponse(list(livros), safe=False)