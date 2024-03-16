
from random import choice
import matplotlib.pyplot as plt


plt.show()


estudantes = ["João", "Maria", "José"]
notas = [8.5, 9, 6.5]


plt.bar(estudantes, notas)


estudantes_2 = ["João", "Maria", "José", "Ana"]


#help(choice)


estudante = choice(estudantes_2)


print("{}".format(choice(estudantes_2)))


#Notas 
notas = {'1 Trimestre': 8.5, '2° Trimestre': 9.5, '3º trimestre': 7}


soma = 0 

for nota in notas.values():
    soma += nota


somatorio = sum(notas.values())


qtd_notas = len(notas)


#media = somatorio / qtd_notas


print("Média {:.2f}".format(somatorio / qtd_notas))


#round?


# ------ criando função sem paramentro ----------
def media():
    calculo = (10 + 9 + 8) /3
    print(calculo)
    

print(media())

# ------ criando função com paramentro ----------
def media(nota_1, nota_2, nota_3):
    calculo = (nota_1 + nota_2 + nota_3) / 3
    print(calculo)


media(3, 6, 9)

print(media)

# ------



def media(lista):
    calculo = sum(lista) / len(lista)
    print(calculo)


media(notas.values())

print(media)


#--------função com return ------------------------------


# Notas do(a) estudante
notas = [8.5, 9.0, 6.0, 10.0]


def media(lista):
    calculo = sum(lista) / len(lista)
    return calculo


resultado = media(notas)

print(resultado)


#--------------------------------------


# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.0]


def boletim(lista):
    media = sum(lista) / len(lista)
    if media >= 6:
        situacao = 'Aprovado(a)'
    else:
        situacao = 'Reprovado(a)'
    return (media, situacao)


#chamando a função e passando a lista de notas
boletim(notas)


media, situacao = boletim(notas)



print(f'O(a) estudante atingiu uma média de {media} e foi {situacao}.')



# --------- Funções lambda -------------------------------


n1 = float(input("Digite a 1º nota: "))

n2 = float(input("Digite a 2º nota: "))

n3 = float(input("Digite a 3º nota: "))


media_ponderavel = lambda x, y, z: (x*3 + y*2 + z*5) / 10

media_estudante = media_ponderavel(n1, n2, n3)



# Exibindo a média
print(f'O(a) estudante atingiu uma média de {media_estudante}')


# --------- Funções lambda com map -------------------------------

#map(<lambda function>, <iterador>)


# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.5, 8.0]

qualitativo = 0.5


#notas_atualizadas = lambda x: x + qualitativo

notas_atualizadas = map(lambda x: x + qualitativo, notas)

print(notas_atualizadas)

notas_atualizadas = list(notas_atualizadas)

print(notas_atualizadas)


