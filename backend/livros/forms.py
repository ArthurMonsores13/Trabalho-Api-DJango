from django import forms
from .models import Livro

GENEROS_SUGERIDOS = [
    'Ficção Científica', 'Fantasia', 'Romance', 'Terror',
    'Suspense', 'Aventura', 'Drama', 'Biografia',
    'História', 'Autoajuda', 'Filosofia', 'Poesia',
]

class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano', 'genero', 'nota', 'comentario']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: O Senhor dos Anéis',
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: J.R.R. Tolkien',
            }),
            'ano': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 1954',
                'min': 1,
                'max': 2100,
            }),
            'genero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Fantasia',
                'list': 'generos-list',
            }),
            'nota': forms.HiddenInput(),
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escreva sua opinião sobre o livro...',
            }),
        }
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'ano': 'Ano de Publicação',
            'genero': 'Gênero',
            'nota': 'Nota',
            'comentario': 'Comentário',
        }
        error_messages = {
            'titulo': {'required': 'O título é obrigatório.'},
            'autor':  {'required': 'O autor é obrigatório.'},
            'ano':    {'required': 'O ano é obrigatório.', 'invalid': 'Digite um ano válido.'},
            'genero': {'required': 'O gênero é obrigatório.'},
        }

    def clean_nota(self):
        nota = self.cleaned_data.get('nota', 0)
        if nota is None:
            nota = 0
        if nota < 0 or nota > 5:
            raise forms.ValidationError('A nota deve ser entre 0 e 5.')
        return nota
