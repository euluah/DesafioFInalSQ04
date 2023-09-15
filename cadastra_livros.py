from reqAPI import cadastraLivro, buscaLivro

livros = [
    {
        "title": "1984",
        "description": "George Orwell",
        "author": 1,
        "gender": 1
    },
    {
        "title": "Duna",
        "description": "Frank Herbert",
        "author": 2,
        "gender": 1
    },
    {
        "title": "O Senhor dos Anéis",
        "description": "J.R.R. Tolkien",
        "author": 3,
        "gender": 2
    },
    {
        "title": "O Código Da Vinci",
        "description": "Dan Brown",
        "author": 4,
        "gender": 3
    }
]

for l in livros:
    cadastraLivro(l)

buscaLivro()
