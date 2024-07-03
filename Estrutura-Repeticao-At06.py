import os
os.system("cls")


print("Exemplo While com texto")
resposta=input("Deseja somar dois números? (sim)  (não)\n").lower()

while resposta == "sim" :
    v1 = int(input("Digite um número:"))
    v2 = int(input("Digite outro número:"))

    resultado= v1 + v2

    print("A Soma dos números é:",resultado)

    resposta=input("Digite (sim) para reiniciar, e (não) para encerrar!\n").lower()

else:
    input("Pressione <enter> para encerrar")
