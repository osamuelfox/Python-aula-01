#Trabalhando com bibliotecas

import math
import os

x = 16 
raizQuad = math.sqrt(x) #Raiz quadrada
print("Raiz quadrada de ",x," é igual a", raizQuad)

angulo = 45
seno = math.sin(angulo) #Seno do angulo
print("O seno de ",angulo," é igual a", seno)

diretorio = os.getcwd()
print("O diretorio corrente é", diretorio) #Irá mostra onde está o diretorio do arquivo em execusao

'''os.system("cls")''' #invoca uma funcao dentro do terminal de comandos

lista = [10, 20, 30]
tam = len(lista) #Irá calcular o tamanho da lista
print("A lista", lista, "tem tamanho", tam)

soma = sum(lista) #Irá somar todos os itens da lista
print("A lista", lista, " tem um somatorio igual a", soma)