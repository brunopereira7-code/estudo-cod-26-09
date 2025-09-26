import os 
os.system("cls") 

pares=0 
impares=0
soma_pares=0
soma_geral=0
contador_geral=0

while True:
    numero=int(input("Digite seu numero:"))

    if numero > 0:
        contador_geral += 1 
        soma_geral += numero
        if numero % 2 == 0:
            pares +=1
        else:
            impares += 1 
            
    if numero == 0:
            break

#calculando 


# if pares !=0:
#      media_pares=soma_pares / pares   coluna 1
# else:
#      media_pares=0 


# if contador_geral != 0:
#      media_geral=soma_geral / contador_geral   coluna 2

# else:
#      media_geral=0


media_pares=soma_pares / pares if pares != 0 else 0 # col 1

media_geral= soma_geral / contador_geral if contador_geral != 0 else 0 # col 2



#calculos 

media_pares=soma_pares/ pares 
media_geral=soma_geral/contador_geral

#exibindo 

print(f"os numeros pares sao {pares}")
print(f"os numeros impares sao {impares}")
print(f"os numeros media pares sao {media_pares}")
print(f"a media é  {media_geral}")
