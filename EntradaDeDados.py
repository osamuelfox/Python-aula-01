#Tipos de Dados
#Python declara automaticamente os tipos de dados recebidos

str #string / Tipo texto
int #numeros inteiros
float #numero com casas decimais ou ponto flutuante
bool #booleano ou logico(true / false)

#Conversão de dados

a = int (5.6565) #Convertando um valor float para int
print(a)

b = str (6.4323) #Convertendo um valor float para text
print(b)

c = float (6) #Convertendo um valor int para float
print(c)

d = bool (1) #Convertendo int para booleanos (Qualquer string é True, exceto strings vazias / Qualquer número é True, exceto 0 / Qualquer lista, tupla, conjunto e dicionário são True, exceto os vazios.  )
print(d)

#Entrada de Dados

x = input("Escreva o seu nome: ") #input Entrada de Dados / input interpreta como tipo str
y = int (input("Escreva a sua idade: "))
z = bool(int(input("Brasileiro: (0)nao / (1)sim: ")))

print("\nSeu nome é: ",x)
print("Sua idade é: ",y)
print("Brasileiro: ",z)

