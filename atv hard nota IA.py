import os
os.system("cls")

print(""" 
 1 - Adicionar pessoa 
 2 - Exibir resultados
 3 - Sair 
""")

# Listas para armazenar os dados
pessoas = []
idades = []
salarios = []
generos = []

while True:
    numero = input("Digite uma opção: ")

    match numero:
        case "1":
            nome = input("Digite o nome da pessoa: ")
            idade = int(input("Digite a idade: "))
            salario = float(input("Digite o salário: "))
            genero = input("Digite o gênero (M/F): ")

            # Salvando dados nas listas
            pessoas.append(nome)
            idades.append(idade)
            salarios.append(salario)
            generos.append(genero)

            print(f"{nome} foi adicionado(a) com sucesso!")

        case "2":
            if len(pessoas) == 0:
                print("Nenhuma pessoa cadastrada ainda.")
            else:
                media_salario = sum(salarios) / len(salarios)
                maior_idade = max(idades)
                menor_idade = min(idades)
                mulheres_50000 = sum(1 for i, g in enumerate(generos) if g.upper() == "F" and salarios[i] >= 50000)

                print(f"Média salarial do grupo: {media_salario:.2f}")
                print(f"Maior idade: {maior_idade}")
                print(f"Menor idade: {menor_idade}")
                print(f"Quantidade de mulheres com salário >= 50000: {mulheres_50000}")

        case "3":
            print("Saindo...") 
            break
         
        case _: 
            print("Digite um dos números válidos (1, 2 ou 3).")  
