## guardei o nome do usuario
anoCorreto = False
nome = input("Qual seu nome completo?")
ano = 2023

##laço de repetição while, repetir até que a variavel seja "TRUE"
while (anoCorreto == False):

   print("Insira um ano de nascimento entre 1922 e 2021")

# Try...Expect para verifiação de erros   
   try:

      anoNascimento = int(input())
      idade = ano - anoNascimento

      if (anoNascimento >= 1922) and (anoNascimento <= 2021):

           anoCorreto = True
         
           print(f"{nome} sua idade é {idade}")   #saída se estiver tudo ok
      else :

           print("Ano de Nascimento inválido!")

   except:
     # caso o usuario digite um texto no campo de ano de Nascimento
       print("Texto é inválido, por favor digite um número válido")
