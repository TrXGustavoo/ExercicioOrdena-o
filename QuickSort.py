from ListaDuplamenteLigada import ListaDuplamenteLigada


def quick_sort(lista_ordernar, tipo_ordenacao='crescente'):
    if lista_ordernar.size() <= 1:
        return lista_ordernar

    pivot = lista_ordernar.tail.value  # Usando o último elemento como pivô
    lista_ordernar.remove(pivot)

    menor = ListaDuplamenteLigada()
    maior = ListaDuplamenteLigada()

    current = lista_ordernar.head
    while current:
        if current.value <= pivot:
            menor.append(current.value)
        else:
            maior.append(current.value)
        current = current.next

    if tipo_ordenacao == 'crescente':
        return concatenate_lists(quick_sort(menor, tipo_ordenacao), pivot, quick_sort(maior, tipo_ordenacao))
    else:
        return concatenate_lists(quick_sort(maior, tipo_ordenacao), pivot, quick_sort(menor, tipo_ordenacao))



def concatenate_lists(menor, pivot, maior):
    result = ListaDuplamenteLigada()

    current = menor.head
    while current:
        result.append(current.value)
        current = current.next

    result.append(pivot)

    current = maior.head
    while current:
        result.append(current.value)
        current = current.next

    return result
