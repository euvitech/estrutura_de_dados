# 1. Criar a Pilha
torre_de_cristais = []

# 2. Empilhar Cristal
def empilhar_cristal(pilha, cristal):
    pilha.append(cristal)

empilhar_cristal(torre_de_cristais, "Cristal do Passado")
empilhar_cristal(torre_de_cristais, "Cristal do Presente")
empilhar_cristal(torre_de_cristais, "Cristal do Futuro")

# 3. Visualizar a Pilha
print("Torre de Cristais inicial:")
print(torre_de_cristais)

# 4. Desempilhar Cristal
def desempilhar_cristal(pilha):
    if pilha:
        return pilha.pop()
    else:
        return "Nenhum cristal disponível."

cristal_utilizado = desempilhar_cristal(torre_de_cristais)
print("\nCristal utilizado no ritual:")
print(cristal_utilizado)

# 5. Verificar Pilha Vazia
def pilha_vazia(pilha):
    return len(pilha) == 0

print("\nA pilha está vazia?")
print(pilha_vazia(torre_de_cristais))

# 6. Visualizar Pilha Restante
print("\nCristais restantes na torre:")
print(torre_de_cristais)

# 7. Desempilhar Cristais Restantes
print("\nUtilizando cristais restantes:")
while not pilha_vazia(torre_de_cristais):
    print("Cristal utilizado:", desempilhar_cristal(torre_de_cristais))

# Verificar novamente se a pilha está vazia
print("\nA pilha está vazia agora?")
print(pilha_vazia(torre_de_cristais))
