class NodeArvore:
    """
    Classe Node para a árvore binária.
    Cada nó possui um valor e referências para os nós esquerdo e direito.
    """
    def __init__(self, valor: int):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def __repr__(self):
        return f"NodeArvore({self.valor})"

class ArvoreBinaria:
    """
    Implementação de uma Árvore Binária de Busca (BST).
    """
    def __init__(self):
        self.raiz = None

    def inserir(self, valor: int) -> None:
        """Insere um valor na árvore binária de busca."""
        self.raiz = self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, node: NodeArvore, valor: int) -> NodeArvore:
        if node is None:
            return NodeArvore(valor)
        if valor < node.valor:
            node.esquerda = self._inserir_rec(node.esquerda, valor)
        elif valor > node.valor:
            node.direita = self._inserir_rec(node.direita, valor)
        # Se o valor for igual, não insere duplicata
        return node

    def em_ordem(self) -> None:
        """Realiza uma travessia em ordem e imprime os valores."""
        self._em_ordem_rec(self.raiz)
        print()

    def _em_ordem_rec(self, node: NodeArvore) -> None:
        if node is not None:
            self._em_ordem_rec(node.esquerda)
            print(node.valor, end=" ")
            self._em_ordem_rec(node.direita)