anoCorreto = False
nome = input("Qual seu nome completo?")
ano = 2023

while (anoCorreto == False):

   print("Insira um ano de nascimento entre 1922 e 2021")

   try:

      anoNascimento = int(input())
      idade = ano - anoNascimento

      if (anoNascimento >= 1922) and (anoNascimento <= 2021):

           anoCorreto = True

           print(f"{nome} sua idade é {idade}")
      else :

           print("Ano de Nascimento inválido!")

   except:

       print("Texto é inválido, por favor digite um número válido")
