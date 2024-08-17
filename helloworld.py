import datetime #importar toda a biblioteca

#Formatando saída de dados com print(f-string)

x = 25.1254          #float
y = "Samuel Santos"  #text
z = 1000             #int
d = datetime.date (2024,10,24)  #date
h = datetime.time (12,45)   #hora

#Formatador Float

print(f"Preço: R$ { x: .2f}" ) #Formantando as casas dercimais

print(f"Preço: R$ { x: e}" ) #Formatando com notação cientifica

print(f"Preço: R$ { x: .2e}" ) #Formatando com notação cientifica com tamanho

#Formatadores inteiros

print(f"Decimal: {z: d}") #Decimal
print(f"Hexadecimal: {z: x}") #Hexadecimal
print(f"Octal: {z: o}") #Octal
print(f"Binario: {z: b}") #Binario

#Formatadores Data e Hora

print(f"Data: {d}") #Formato USA
print(f"Data: {d: %d-%m-%y}") #Formato BR
print(f"Data: {d: %d-%m-%y}, Hora: {h: %H:%M}") #Formato Data e Hora

#Formatando Data e Hora Atual

hoje = datetime.date.today() #Data atual
print("Data atual: ",hoje)

hora = datetime.datetime.now() #Data e hora Atual
print("Data e hora atual",hora)

print (f"Hora atual: {hora: %H:%M}") #Hora Atual
#Saida de Dados: Caracteres Especiais

print("\\") #Barra invertida
print("\'") #Aspa simples
print("\"") #Aspa duplas
print("\n") #Nova Linha
print("\t") #Tab
