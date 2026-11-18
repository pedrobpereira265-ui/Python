from datetime import date, timedelta

# Peça a nota de um aluno (0 a 10) e mostre: Aprovado (≥ 7), Recuperação (≥ 5 e < 7) ou 
# Reprovado (< 5).
# Peça um número inteiro e diga se ele é par ou ímpar (dica: operador %).
# Peça o ano de nascimento e a idade atual, e informe se a pessoa pode dirigir (18 ou mais). 
# Use f-string na resposta.

nota = int(input("Digite a sua nota (0 a 10): "))

if nota >= 7:
    print(f"Parabéns!! Você foi aprovado!")

elif 5 <= nota < 7:
    print(f"Precisa realizar a Recuperação!!")
    
else:
    print(f"Está reprovado!!")
    
#-------------PAR OU IMPAR------------------
    
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"seu número escolhido ({numero}) é Par!")
    
else:
    print(f"seu número escolhido ({numero}) é Impar")
    
#-------------------- PODE DIRIGIR OU NÃO -------------------

idade = int(input("Digite a sua idade: "))
ano = int(input("Digite o ano de nascimento: "))
hoje = date.today().year - ano

if idade >= 18 and hoje >= 18:
    print(f"Parabéns! Você pode dirigir, seu vagabundo!")
    
elif idade >= 16 and hoje >= 16:
    print(f"Bom! Você pode votar, mas não dirigir!!")
    
else:
    print(f"Vá para casa PIRRALHO!")
    
# --------------TESTE---------------

#resposta: Bom, ele retornara o primeiro, pois o sistema le de cima para baixo e
# como o primeiro if é mostrado, ele também será o primeiro a mostrar, já que todos são
# verdadeiros. Ou será mostrado o else.

x = 10
if x > 5:
    print("A")
if x > 8:
    print("B")
elif x > 9:
    print("C")
else:
    print("D")