#Operacoes aritmeticas com atribuicao

x = 5

x += 1 #Soma +1 na variavel x 5+1 = 6
x -= 1 #Subtrai -1 na varial x 6-1 = 5
x *= 2 #multiplica *2 na variavel x 5*2 = 10
x /= 2 #Divite /2 na variavel x 10/2 = 5
x %= 2 #Resto da divisao 5 mod 2 = 1

#Calculadora simples

a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print("\nResultados\n")
print("Soma: ", soma)
print("Subtracao", subtracao)
print("Multiplicacao", multiplicacao)
print("Divisao", divisao)
print("Resto da divisao", resto)

#Area de um triangulo

print("\nCalculo da area de um triangulo\n")

base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))
resultado = (base * altura)/2

print("A area do triangulo é de: ",resultado)