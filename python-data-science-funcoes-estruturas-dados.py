

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




