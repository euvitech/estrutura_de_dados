class ListaOrdenada:
    """
    Implementação de uma lista ordenada (em ordem crescente).
    Assume que os itens são comparáveis (por exemplo, números).
    """
    class Node:
        def __init__(self, data: any):
            self.data = data
            self.next = None

        def __repr__(self):
            return f"Node({self.data})"

    def __init__(self):
        self.head = None

    def insere_ordenado(self, data: any) -> None:
        """Insere um data na lista mantendo a ordem crescente."""
        novo = ListaOrdenada.Node(data)
        if self.head is None or data < self.head.data:
            novo.next = self.head
            self.head = novo
        else:
            atual = self.head
            while atual.next is not None and atual.next.data < data:
                atual = atual.next
            novo.next = atual.next
            atual.next = novo

    def imprime_lista(self) -> None:
        """Imprime os itens da lista ordenada."""
        atual = self.head
        elementos = []
        while atual:
            elementos.append(str(atual.data))
            atual = atual.next
        print(" -> ".join(elementos) + " -> None")