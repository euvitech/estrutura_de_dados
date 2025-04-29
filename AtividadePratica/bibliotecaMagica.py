# 1. Criar o Catálogo
catalogo_magico = []

# 2. Adicionar Livros
def adicionar_livro(catalogo, livro):
    catalogo.append(livro)

adicionar_livro(catalogo_magico, "O Feitiço da Lua Crescente")
adicionar_livro(catalogo_magico, "A Jornada do Unicórnio Perdido")
adicionar_livro(catalogo_magico, "Segredos da Floresta Encantada")

# 3. Visualizar o Catálogo
print("Catálogo inicial:")
print(catalogo_magico)

# 4. Buscar Livro por Posição
def buscar_livro(catalogo, indice):
    if 0 <= indice < len(catalogo):
        return catalogo[indice]
    else:
        return "Índice fora do intervalo."

livro_encontrado = buscar_livro(catalogo_magico, 1)
print("\nLivro na posição 1:")
print(livro_encontrado)

# 5. Remover Livro
catalogo_magico.remove("A Jornada do Unicórnio Perdido")

# 6. Visualizar Catálogo Atualizado
print("\nCatálogo após remoção:")
print(catalogo_magico)

# 7. Verificar Presença
def verificar_livro(catalogo, livro):
    return livro in catalogo

presenca = verificar_livro(catalogo_magico, "Segredos da Floresta Encantada")
print("\n'\"Segredos da Floresta Encantada\" está no catálogo?")
print(presenca)
