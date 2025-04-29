from ListasEncadeadas.listaEncadeada import ListaSimples
from ListasOrdenadas.listaOrdenada import ListaOrdenada
from ArvoresBinarias.arvoreBinaria import ArvoreBinaria

def main():
    print("====== Teste de Listas Encadeadas ======")
    lista = ListaSimples()
    print("Inserindo elementos na lista:")
    lista.insere_inicio(10)
    lista.insere_fim(20)
    lista.insere_inicio(5)
    lista.imprime_lista()
    
    print("Removendo elemento do início:", lista.remove_inicio())
    lista.imprime_lista()
    
    resultado_busca = lista.busca(20)
    print("Resultado da busca pelo elemento 20:", resultado_busca)
    
    print("\n====== Teste de Listas Ordenadas ======")
    lista_ord = ListaOrdenada()
    for valor in [50, 20, 40, 10, 30]:
        lista_ord.insere_ordenado(valor)
    lista_ord.imprime_lista()
    
    print("\n====== Teste de Árvores Binárias ======")
    arvore = ArvoreBinaria()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arvore.inserir(valor)
    print("Árvore em ordem (In-order traversal):")
    arvore.em_ordem()

if __name__ == "__main__":
    main()