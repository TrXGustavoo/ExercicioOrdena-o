from ListaDuplamenteLigada import ListaDuplamenteLigada


def bubble_sort(lista_ordernar, tipo_ordenacao):
    tam = lista_ordernar.size()

    for i in range(tam):
        current = lista_ordernar.head
        for n in range(0, tam - 1 - i):
            if tipo_ordenacao == "crescente":
                if current.value > current.next.value:
                    temp = current.value
                    current.value = current.next.value
                    current.next.value = temp
            elif tipo_ordenacao == "decrescente":
                if current.value < current.next.value:
                    temp = current.value
                    current.value = current.next.value
                    current.next.value = temp
            current = current.next
