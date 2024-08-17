#Trabalhando com Operadores Relacionais 

#Maior > 
#Menor <
#Maior ou igual >=
#Menor ou igual <= 
#Igual ==
#Diferente !=

#Operadores Logicos

#Negacao / inversao (not) "nao" inverte o valor logico

#Conjuncao (and) "e" resulta em True quando tudo é True, False caso contrario

#Disjuncao (or) "ou" resulta em True quando ao menos um é True, False caso contrario

#Operador In 

#Verifica se um item pertence em um conjunto de itens - if <elemento> in <lista, tuples, etc>: 

print("Boletin")
x = float(input("\nDigite sua nota: "))

if x < 4: 
    print("Reprovado")
elif x <7:
    print("Recuperacao")
elif x <=10:
    print("Aprovado")
else:
    print("Nota invalida")

#Outro modo de fazer

if x >= 4 and x < 7:
    print("Tem direito a fazer a fazer um teste")

elif x >= 7 and x <= 10:
    print("Passou de ano")

elif x < 4 or x > 0:
    print("Reprovado")
   
else:
    print("Nota deve ser de 0 ate 10")
