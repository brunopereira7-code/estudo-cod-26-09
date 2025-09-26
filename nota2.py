import os 
os.system("cls") 


soma=0


while True:
    nota_1=float(input("Digite sua nota:"))
    nota_2=float(input("Digite sua nota:"))
    
    soma+=nota_1+nota_2


    continuar= input("digite sim ou nao pra continuar ").lower()
    if continuar == "nao":
        print("ok") 
        break 

media=soma / 2
    

print(f"sua media é {media}")