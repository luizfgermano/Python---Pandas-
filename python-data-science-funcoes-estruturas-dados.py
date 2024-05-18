
from random import choice
import matplotlib.pyplot as plt
from random import randint


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



#----------------------------------------------------------


notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]


nomes = []

notas_juntas = []


for i in range(len(notas_turma)):
    if i % 4 ==0:
        nomes.append(notas_turma[i])
    else:
        notas_juntas.append(notas_turma[i])


print(nomes)

print(notas_juntas)


notas = []

for i in range(0, len(notas_juntas), 3):
    notas.append([notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]])


print(notas)

print(notas[0])

print(notas[0][2])


#---------------------------------------------------------------------


estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]


def gerar_codigo():
    return str(randint(0, 999))




codigo_estudantes = []


for i in range(len(estudantes)):
    #criando uma tupla e adicionando infomação
    codigo_estudantes.append((estudantes[i], estudantes[i][0] + gerar_codigo()))



print(codigo_estudantes)


#----------------------------------------------------------------------------


notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]


def media(lista: list=[0]) -> float:
  ''' Função para calcular a média de notas passadas por uma lista

  lista: list, default [0]
    Lista com as notas para calcular a média
  return = calculo: float
    Média calculada
  '''
  
  calculo = sum(lista) / len(lista)

  return calculo


medias = [round(media(nota),1) for nota in notas]


print(medias)


nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]


nomes = [nome[0] for nome in nomes]

print(nomes)




#-----------------------------------------
estudantes = zip(nomes, medias)

print(estudantes)

#quando foi printa a variavel estudantes mostro o lugar da memoria armazenado 
#precisando muda para uma listapara conseguir ver o conteudo
estudantes = list(zip(nomes, medias))

print(estudantes)
#-----------------------------------------

#gerando uma lista de pessoas candidatas a bolsa
candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]

print(candidatos)



#--------------------------------------------------------------------------


nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]


situacao = ["Aprovado" if media >=6 else "Reprovado" for media in medias]

'''
# fazendo um for de outra maneira, de vez a de cima.
for i in medias:
    if i >=6:
        print("aprovado")
    else:
        print("reprovado")
'''

print(situacao)

cadastro = [x for x in [nomes, notas, medias]]
print(cadastro)

lista_completa = [nomes, notas, medias, situacao]
print(lista_completa)


# Dict comprehension --------------------------------------------------------

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]


coluna = ["Notas", "Media Final", "Situação"]

cadastro = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))}

print(cadastro)


cadastro["Estudante"]


cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]

print(cadastro)


# Tratando exceções com try e except ---------------------------------------------

'''

try:
    # código a ser executado. Caso uma exceção seja lançado, pare imediatamente
except:
    #Se a exceção for lançada no try, role esse código, senão pule  esta etapa       

'''


notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}


nome = input("DIgite o nome do estudate: ")

resultado = notas[nome]

print(resultado)


try:
    nome = input("DIgite o nome do estudate: ")
    resultado = notas[nome]
except Exception as e:
    print(type(e), f"Erro: {e}")



try:
    nome = input("DIgite o nome do estudate: ")
    resultado = notas[nome]
except KeyError:
    print("Estudante não matriculado(a) na turma")



notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],
    'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0],
    'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}



try:
    nome = input("DIgite o nome do estudate: ")
    resultado = notas[nome]
except KeyError:
    print("Estudante não matriculado(a) na turma")
else:
   print(resultado)



# usando Cláusula finally


notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}


try:
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]
except KeyError:
    print("Estudante não matriculado(a) na turma")
else:
    print(resultado)
finally:
    print("A consulta foi encerrada!")
























