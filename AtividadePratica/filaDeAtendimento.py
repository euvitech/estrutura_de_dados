from collections import deque

# 1. Criar a Fila
fila_de_pedidos = deque()

# 2. Adicionar Pedidos
def adicionar_pedido(fila, pedido):
    fila.append(pedido)

adicionar_pedido(fila_de_pedidos, "Martelo Encantado")
adicionar_pedido(fila_de_pedidos, "Pinça Teleportadora")
adicionar_pedido(fila_de_pedidos, "Chave de Fenda Sônica")

# 3. Visualizar a Fila
print("Fila de pedidos inicial:")
print(fila_de_pedidos)

# 4. Processar Pedido
def processar_pedido(fila):
    if fila:
        return fila.popleft()
    else:
        return "Nenhum pedido para processar."

pedido_atendido = processar_pedido(fila_de_pedidos)
print("\nPedido atendido:")
print(pedido_atendido)

# 5. Verificar Fila Vazia
def fila_vazia(fila):
    return len(fila) == 0

print("\nA fila está vazia?")
print(fila_vazia(fila_de_pedidos))

# 6. Visualizar Fila Restante
print("\nPedidos restantes na fila:")
print(fila_de_pedidos)

# 7. Processar Pedidos Restantes
print("\nProcessando pedidos restantes:")
while not fila_vazia(fila_de_pedidos):
    print("Pedido atendido:", processar_pedido(fila_de_pedidos))

# Verificar novamente se a fila está vazia
print("\nA fila está vazia agora?")
print(fila_vazia(fila_de_pedidos))
