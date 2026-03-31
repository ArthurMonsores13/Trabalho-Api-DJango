
from django.contrib import admin
from django.urls import path
from livros.views import mostrar_livros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/',mostrar_livros),
    path('livros/<str:genero>/', mostrar_livros)
]
