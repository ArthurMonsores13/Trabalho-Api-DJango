# 📚 Minha Biblioteca

Aplicação web de catálogo pessoal de livros desenvolvida com **Django**. Permite cadastrar, visualizar, editar e excluir livros do seu acervo, com suporte a notas por estrelas, comentários e filtros por gênero.

---

## ✨ Funcionalidades

- **Acervo visual** — listagem de livros em cards com lombada colorida, estrelas e preview do comentário
- **Busca** — pesquise por título ou autor diretamente na barra de pesquisa
- **Filtro por gênero** — filtre rapidamente os livros por categoria
- **Adicionar livro** — formulário com seletor de estrelas interativo (clique nas ⭐ para dar nota)
- **Editar livro** — atualize qualquer informação de um livro existente
- **Excluir livro** — página de confirmação antes de remover do acervo
- **API JSON** — endpoints REST para integração com outras ferramentas.

---

## 🖥️ Como rodar

**Pré-requisitos:** Python 3.10+

```bash
# 1. Clone / acesse o projeto
cd trab-backend

# 2. Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Acesse a pasta do projeto Django
cd backend

# 5. Aplique as migrações
python manage.py migrate

# 6. (Opcional) Crie um superusuário para o admin
python manage.py createsuperuser

# 7. Rode o servidor
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000/**

---

## 🗺️ Rotas

### Interface Web (HTML)

| Rota | Descrição |
|---|---|
| `/` | Redireciona para o acervo |
| `/livros/` | Lista todos os livros (com busca e filtro) |
| `/livros/<id>/` | Detalhes de um livro |
| `/livros/adicionar/` | Formulário para novo livro |
| `/livros/<id>/editar/` | Formulário para editar livro |
| `/livros/<id>/deletar/` | Página de confirmação de exclusão |
| `/admin/` | Painel administrativo do Django |

### API JSON

| Rota | Descrição |
|---|---|
| `/api/livros/` | Retorna todos os livros em JSON |
| `/api/livros/<genero>/` | Filtra livros por gênero (ex: `/api/livros/Romance/`) |
| `/api/livros/?genero=X` | Filtra livros por gênero via query param |

**Exemplo de resposta da API:**
```json
[
  {
    "id": 1,
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "ano": 1954,
    "genero": "Fantasia",
    "nota": 5,
    "comentario": "Uma obra-prima absoluta."
  }
]
```

---

## 🗂️ Estrutura do projeto

```
trab-backend/
├── backend/
│   ├── catalogo/           # Configurações do projeto Django
│   │   ├── settings.py
│   │   └── urls.py
│   └── livros/             # App principal
│       ├── models.py       # Modelo Livro
│       ├── views.py        # Views HTML + API JSON
│       ├── forms.py        # Formulário de livro
│       ├── admin.py        # Registro no admin
│       ├── templatetags/   # Filtro custom de estrelas
│       └── templates/
│           └── livros/
│               ├── base.html     # Layout base (navbar, footer)
│               ├── lista.html    # Listagem com busca e filtro
│               ├── detalhe.html  # Página do livro
│               ├── form.html     # Adicionar / Editar
│               └── deletar.html  # Confirmação de exclusão
├── requirements.txt
└── README.md
```

---

## 🛠️ Tecnologias

- **Django 6** — framework web backend
- **SQLite** — banco de dados (arquivo local `db.sqlite3`)
- **Bootstrap 5** — design responsivo via CDN
- **Bootstrap Icons** — ícones via CDN

---

## 📖 Modelo de dados

O modelo `Livro` possui os seguintes campos:

| Campo | Tipo | Descrição |
|---|---|---|
| `titulo` | CharField(200) | Título do livro |
| `autor` | CharField(100) | Nome do autor |
| `ano` | IntegerField | Ano de publicação |
| `genero` | CharField(50) | Gênero literário |
| `nota` | IntegerField (0–5) | Avaliação em estrelas |
| `comentario` | CharField(500) | Comentário pessoal |
