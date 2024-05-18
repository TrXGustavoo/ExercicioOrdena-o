from ListaDuplamenteLigada import ListaDuplamenteLigada


def insert_sort(lista_ordernar, tipo_ordenacao):
    tam = lista_ordernar.size()
    for i in range(1, tam):
        current = lista_ordernar.head
        for _ in range(i):
            current = current.next

        key = current.value
        j = i - 1

        while j >= 0 and ((tipo_ordenacao == 'crescente' and key < current.prev.value) or \
              (tipo_ordenacao == 'decrescente' and key > current.prev.value)):
            current.value = current.prev.value
            current = current.prev
            j -= 1

        current.value = key
    return lista_ordernar
