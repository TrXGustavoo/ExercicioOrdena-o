from bubbleSort import bubble_sort
from insertSort import insert_sort
from ListaDuplamenteLigada import ListaDuplamenteLigada
from QuickSort import quick_sort


def ordenar_lista(lista_numerica, metodo, tipo):
    if metodo == 'B':
        bubble_sort(lista_numerica, tipo)
        return print(f'Lista ordenada: {lista_numerica.display()}')
    elif metodo == 'I':
        insert_sort(lista_numerica, tipo)
        return print(f'Lista ordenada: {lista_numerica.display()}')
    elif metodo == 'Q':
        lista_ordenada = quick_sort(lista_numerica, tipo)
        return print(f'Lista ordenada: {lista_ordenada.display()}')


lista_numerica = ListaDuplamenteLigada()
while True:
    try:
        numero = int(input("Digite um numero para adicionar a lista: "))
    except ValueError:
        print("Digite um numero inteiro")
        continue
    lista_numerica.append(numero)
    op = str(input("Deseja adicionar mais um numero? [S/N]: ")).upper().strip()[0]
    tam_lista_numerica = lista_numerica.size()
    if op == "N" and tam_lista_numerica > 1:
        break
    elif op == "N" and tam_lista_numerica <= 1:
        print("A lista dever ter pelo menos 2 numeros")

print(f'Lista nao ordenada: {lista_numerica.display()}')

while True:
    metodo_ordenacao = input(
        "\nQual metodo de ordenação deseja usar?\n[B] Bubble Sort\n[Q] Quick Sort\n[I] Insert Sort\n"
    ).upper().strip()
    if metodo_ordenacao in ['B', 'Q', 'I']:
        break
    else:
        print("Entrada inválida. Por favor, escolha 'B', 'Q' ou 'I'.")

while True:
    ordem_ordenacao = input(
        "Qual metodo de classificação deseja usar (crescente/decrescente)? "
    ).lower().strip()
    if ordem_ordenacao in ['crescente', 'decrescente']:
        break
    else:
        print("Entrada inválida. Por favor, escolha 'crescente' ou 'decrescente'.")

ordenar_lista(lista_numerica, metodo_ordenacao, ordem_ordenacao)
