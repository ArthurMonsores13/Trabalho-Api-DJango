from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

from livros.views import (
    lista_livros,
    detalhe_livro,
    adicionar_livro,
    editar_livro,
    deletar_livro,
    api_livros,
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Página inicial — redireciona para o acervo
    path('', lambda req: redirect('/livros/'), name='home'),

    # ─── Vistas HTML ───────────────────────
    path('livros/',                    lista_livros,    name='lista_livros'),
    path('livros/adicionar/',          adicionar_livro, name='adicionar_livro'),
    path('livros/<int:pk>/',           detalhe_livro,   name='detalhe_livro'),
    path('livros/<int:pk>/editar/',    editar_livro,    name='editar_livro'),
    path('livros/<int:pk>/deletar/',   deletar_livro,   name='deletar_livro'),

    # ─── API JSON ──────────────────────────
    path('api/livros/',                api_livros,      name='api_livros'),
    path('api/livros/<str:genero>/',   api_livros,      name='api_livros_genero'),
]
