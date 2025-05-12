from main import analisar_lista

lista = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]

media, maior, menor, pares = analisar_lista(lista)

print(f"Média: {media:.1f}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Quantidade de pares: {pares}")
