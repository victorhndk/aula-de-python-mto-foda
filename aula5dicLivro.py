livro = {
    "titulo": "O Pequeno Príncipe",
    "autor": "Antoine de Saint-Exupéry",
    "ano_publicacao": "1943",
    "genero": "Fábula"
}

print(f"Título: {livro['titulo']}")
print(f"Autor: {livro.get('autor')}")
print(f"Ano de Publicação: {livro['ano_publicacao']}")
print(f"Gênero: {livro['genero']}")
