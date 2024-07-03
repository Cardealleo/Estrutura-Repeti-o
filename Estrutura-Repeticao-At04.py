import os
os.system("cls")

print("Exemplo usando Continue!")

i=0

while i<6:
    i+= 1 

    if i ==3:
        continue  #Ele faz pular a condição if

    print(i)