def analisar_lista(lista):
    media = sum(lista) / len(lista)
    maior = max(lista)
    menor = min(lista)
    pares = len([num for num in lista if num % 2 == 0])
    
    return media, maior, menor, pares
