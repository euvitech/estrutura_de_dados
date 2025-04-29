# Lista de Revisão para Prova de Estrutura de Dados I utilizando a linguagem Python

## Listas (Arrays Dinâmicos)

- Criação e manipulação de listas.
- Acesso a elementos por índice.
- Slicing de listas.
- Métodos importantes de listas:
  - `append()`, `insert()`, `remove()`, `pop()`, `index()`, `count()`, `sort()`, `reverse()`, `clear()`, `copy()`.
- List comprehensions.
- Diferenças entre listas e tuplas.

## Filas (Queues)

- Conceito de FIFO (First-In, First-Out).
- Implementação de filas usando listas (com suas limitações de performance para `pop(0)` e `insert(0)`).
- Uso da classe `collections.deque` para implementações eficientes de filas.
- Operações básicas de filas:
  - `enqueue` (adicionar)
  - `dequeue` (remover)
  - `peek` (espiar)
  - `is_empty` (verificar se está vazia)
  - `size` (tamanho)

## Pilhas (Stacks)

- Conceito de LIFO (Last-In, First-Out).
- Implementação de pilhas usando listas (aproveitando os métodos `append()` e `pop()`).
- Operações básicas de pilhas:
  - `push` (empilhar)
  - `pop` (desempilhar)
  - `peek` (topo)
  - `is_empty` (vazia)
  - `size` (tamanho)

## Vetores (Arrays)

- Conceito de arrays (sequências de elementos do mesmo tipo).
- Utilização do módulo `array` do Python para criar arrays de tipos específicos.
- Operações básicas com arrays: acesso, iteração.
- Vantagens e desvantagens em relação a listas:
  - Tipo fixo
  - Geralmente mais eficientes em termos de memória para grandes quantidades de dados do mesmo tipo.

## Matrizes (Arrays Bidimensionais)

- Representação de matrizes usando listas de listas em Python.
- Acesso a elementos em matrizes (linha e coluna).
- Iteração sobre matrizes.
- Operações básicas com matrizes:
  - Adição
  - Multiplicação (conceitualmente)
- Utilização da biblioteca **NumPy** para manipulação eficiente de arrays multidimensionais (conceitos básicos).

---

## Questões de Múltipla Escolha

**1. Qual das seguintes estruturas de dados segue o princípio LIFO (Last-In, First-Out)?**

a) Fila  
b) Lista  
c) **Pilha**  
d) Vetor

**2. Qual método é comumente usado para adicionar um elemento ao final de uma lista em Python?**

a) insert()  
b) add()  
c) **append()**  
d) extend()

**3. Qual das seguintes operações remove e retorna o elemento do início de uma fila implementada com uma lista padrão do Python?**

a) pop()  
b) **pop(0)**  
c) dequeue()  
d) remove(0)

**4. Qual módulo do Python é mais eficiente para criar arrays de tipos numéricos específicos?**

a) collections  
b) **array**  
c) numpy  
d) math

**5. Como você acessaria o elemento na segunda linha e terceira coluna de uma matriz chamada `matriz` representada como uma lista de listas em Python?**

a) **matriz[1][2]**  
b) matriz[2][1]  
c) matriz(2, 3)  
d) matriz{2, 3}

# Questões de Análise de Código

Analise o código Python a seguir e determine a saída ou o comportamento esperado.

---

## Questão 1 (Listas)

```python
numeros = [10, 20, 30, 40, 50]
numeros.insert(2, 25)
del numeros[4]
print(numeros)
```

**Saída esperada:**

```
[10, 20, 25, 30, 50]
```

---

## Questão 2 (Pilhas)

```python
pilha = []
pilha.append(1)
pilha.append(2)
pilha.append(3)
pilha.pop()
pilha.append(4)
print(pilha)
```

**Saída esperada:**

```
[1, 2, 4]
```

---

## Questão 3 (List Comprehension)

Código implícito:

```python
[x**2 for x in range(5) if x % 2 == 0]
```

**Saída esperada:**

```
[0, 4, 16]
```

---

## Questão 4 (Matrizes)

Código implícito:

```python
matriz = [[5, 10], [15, 20]]
print(matriz[1][0])
```

**Saída esperada:**

```
15
```

---

## Questão 5 (Filas com deque)

Código implícito:

```python
from collections import deque
fila = deque()
fila.append(100)
fila.popleft()
fila.append(50)
fila.append(200)
fila.append(300)
print(list(fila))
```

**Saída esperada:**

```
[50, 200, 300]
```