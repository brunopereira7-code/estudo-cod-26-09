import os 
os.system("cls") 


print(""" 
    ------Menu--------
 1- Adicionar pessoa 
 2- Exibir resultados
 3-sair 
      """) 


media_salario_grupo=4.0000
media_maior_idade= 50 
media_menor_idade= 20
quantidades_de_mulheres_com_salarios_50000= 60


while True:
    numero= input("digite uma opçao:")

    match numero:
        case "1":
          adicionar= input("Qual pessoa voce gostaria de adicionar")
          print(f"pessoa {adicionar} adicionada")  
        
        case "2":
        
          print(f"a media do salario  é {media_salario_grupo :2f}")
          print(f"a media de maior de idade é {media_maior_idade}")
          print(f"a media de menor de idade é  {media_menor_idade}")
          print(f"a quantidade esta entre {quantidades_de_mulheres_com_salarios_50000}")

        case "3":
         
         print("Saindo...") 
         break
         
        case _: 
         print("digite um dos numeros pfvr ") 


       

          
      
      
      
       