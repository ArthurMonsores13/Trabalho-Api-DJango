from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Livro
from .forms import LivroForm


# ─────────────────────────────────────────
#  Vistas HTML
# ─────────────────────────────────────────

def lista_livros(request):
    """Lista todos os livros com busca e filtro por gênero."""
    busca = request.GET.get('q', '').strip()
    genero_ativo = request.GET.get('genero', '').strip()

    livros = Livro.objects.all().order_by('titulo')

    if busca:
        livros = livros.filter(titulo__icontains=busca) | \
                 Livro.objects.filter(autor__icontains=busca).order_by('titulo')
        livros = livros.distinct()

    if genero_ativo:
        livros = livros.filter(genero__iexact=genero_ativo)

    generos = Livro.objects.values_list('genero', flat=True).distinct().order_by('genero')

    context = {
        'livros': livros,
        'generos': generos,
        'busca': busca,
        'genero_ativo': genero_ativo,
        'total_livros': Livro.objects.count(),
    }
    return render(request, 'livros/lista.html', context)


def detalhe_livro(request, pk):
    """Exibe os detalhes de um livro específico."""
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livros/detalhe.html', {'livro': livro})


def adicionar_livro(request):
    """Formulário para adicionar um novo livro."""
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save()
            messages.success(request, f'"{livro.titulo}" foi adicionado ao acervo com sucesso!')
            return redirect('detalhe_livro', pk=livro.pk)
    else:
        form = LivroForm()

    return render(request, 'livros/form.html', {'form': form, 'editando': False})


def editar_livro(request, pk):
    """Formulário para editar um livro existente."""
    livro = get_object_or_404(Livro, pk=pk)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{livro.titulo}" foi atualizado com sucesso!')
            return redirect('detalhe_livro', pk=livro.pk)
    else:
        form = LivroForm(instance=livro)

    return render(request, 'livros/form.html', {
        'form': form,
        'livro': livro,
        'editando': True,
    })


def deletar_livro(request, pk):
    """Página de confirmação e exclusão de um livro."""
    livro = get_object_or_404(Livro, pk=pk)

    if request.method == 'POST':
        titulo = livro.titulo
        livro.delete()
        messages.success(request, f'"{titulo}" foi removido do acervo.')
        return redirect('lista_livros')

    return render(request, 'livros/deletar.html', {'livro': livro})


# ─────────────────────────────────────────
#  API JSON (mantida do projeto original)
# ─────────────────────────────────────────

def api_livros(request, genero=None):
    """
    Retorna os livros em formato JSON.
    GET /api/livros/              -> todos os livros
    GET /api/livros/<genero>/     -> filtro por gênero
    GET /api/livros/?genero=X     -> filtro por query param
    """
    if not genero:
        genero = request.GET.get('genero')

    if genero:
        livros = Livro.objects.filter(genero__iexact=genero).values()
    else:
        livros = Livro.objects.all().values()

    if not livros.exists():
        return JsonResponse({'mensagem': 'Nenhum livro encontrado'}, status=404)

    return JsonResponse(list(livros), safe=False)
