class Node:
    """
    Classe Node para listas encadeadas.
    Cada nó contém um valor (data) e uma referência para o próximo nó.
    """
    def __init__(self, data: any):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"
