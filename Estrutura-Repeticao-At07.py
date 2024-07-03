import os

os.system("cls")

print("Contador de Numeros")
valor1= int (input("Digite o Primeiro numero: \n"))
valor2= int (input("Digite o Segundo numero: \n"))

if valor1 > valor2:
    valormaior = valor1
    valormenor = valor2
    
elif valor1 < valor2:
    valormaior = valor2
    valormenor = valor1

else:
    print ("Os numeros são Iguais!")

contador = valormenor

while contador <= valormaior:
    print ("numero: ", contador)
    contador = contador +1
    
else:
    input ("Digite <ENTER> para encerrar ...")