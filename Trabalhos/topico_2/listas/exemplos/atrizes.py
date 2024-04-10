import random

# ==================
# Exemplo 1 do livro
# ==================
# atrizes = ["Paolla de Oliveira", "Camila Queiroz"]
# while True:
#     nome = input("Digite o nome de uma atriz: ")
#     atrizes.append(nome)
#     resp = input("Deseja continuar [S|N]? ")
#     if resp.upper() == "N":
#         break
# print(atrizes)
# print(atrizes[0] + ",", atrizes[1])

# ==================
# Exemplo 2 do livro
# ==================
# atrizes = ["Paolla de Oliveira"]
# atrizes.append("Sheron Menezes")
# atrizes.insert(1, "Raquel Nunes")
# print(atrizes)


# ==================
# Exemplo 3 do livro
# ==================
# atrizes = ["Adriana Prado", "Bárbara Borges", "Camila Queiroz",
# "Danielle Winits", "Fernanda Paes Leme", "Helena Ranaldi",
# "Paolla de Oliveira", "Raquel Nunes", "Viola Davis"]
# random.shuffle(atrizes) #Embaralha a lista
# print(f"Lista embaralhada: {atrizes}")
# sorteada = random.choice(atrizes) #Sorteia aleatoriamente
# print(F"Atriz sorteada: {sorteada}")


# ==================
# Exemplo 4 do livro
# ==================
# atrizes = ["Adriana Prado", "Bárbara Borges", "Camila Queiroz",
#            "Danielle Winits", "Fernanda Paes Leme", "Helena Ranaldi",
#            "Paolla de Oliveira", "Raquel Nunes", "Viola Davis"]
# # Embaralha elementos
# random.shuffle(atrizes)
# print("Lista Embaralhada", atrizes)
# # Ordena elementos crescentemente
# atrizes.sort()  # mesmo que usar
# print("Ordena elementos crescentemente", atrizes)
# # Ordena elementos decrescentemente
# atrizes.sort(reverse=True)
# print("Ordena elementos decrescentemente", atrizes)


# ==================
# Exemplo 5 do livro
# ==================
# atrizes = ["Adriana", "Adriana", "Camila",
#            "Danielle", "Fernanda", "Helena",
#            "Paolla", "Raquel", "Viola"]
#
# print("Removendo a primeira ocorrência do elemento Adriana...")
# atrizes.remove("Adriana")
# print(atrizes)
#
# print("Removendo o elemento de índice 1, que é Camila...")
# atrizes.pop(1)
# print(atrizes)
#
# print("Índice não foi informado. Remove o último elemento: Viola")
# atrizes.pop()
# print(atrizes)
#
# print("Removendo o novo elemento de índice 1, que é Danielle...")
# del atrizes[1]
# print(atrizes)
#
# del atrizes  # Destroi a variável atrizes


# ==================
# Exemplo 6 do livro
# ==================
# atrizes = ["Adriana", "Adriana", "Camila",
#            "Danielle", "Fernanda", "Helena",
#            "Paolla", "Raquel", "Viola"]
#
# copia = list(atrizes)
# print("Lista Original", atrizes)
# print("Cópia da lista atrizes", copia)


# ==================
# Exemplo 7 do livro
# ==================
# atrizes = ["Adriana Prado", "Bárbara Borges", "Camila Queiroz",
#            "Danielle Winits", "Fernanda Paes Leme", "Helena Ranaldi",
#            "Paolla de Oliveira", "Raquel Nunes", "Viola Davis"]
#
# backup = list(atrizes)
#
# # Verifica se a cópia é igual à original
# if backup == atrizes:
#     atrizes.clear()
#     print("Lista de atrizes esvaziada")
# else:
#     print("ERRO: Cópia gerada não é igual à original")


# ==================
# Exemplo 8 do livro
# ==================

atrizes = ["Adriana", "Bárbara", "Camila", "Danielle", "Fernanda"]
print("Atrizes: ", atrizes)

atrizes_internacionais = ["Angelina", "Viola"]
print("Atrizes Internacionais: ", atrizes_internacionais)

atrizes.extend(atrizes_internacionais)
print("Nome de todas as atrizes: ", atrizes)
