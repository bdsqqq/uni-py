# Questão 3(1,25pts) –Faça um programa no Python que solicite ao usuário o salário bruto(sbruto)de um funcionário e, calcule e mostre o salário líquido(sliquido) a receber. Sabe-se que este é composto pelo salário bruto com desconto de 11%.
# sliquido = sbruto-sbruto*0.11
# e acrescido de gratificação, conforme a tabela a seguir
# SalárioLíquido                | Gratificação
# < R$ 1.000,00                 | R$ 200,00
# >=R$ 1.000,00 e < R$ 1.250,00 | R$ 150,00
# >=R$ 1.250,00 e < R$ 1.750,00 | R$ 100,00
# >= R$ 1.750,00                | R$ 75,00
# sliquido = sliquido + gratificacao
# Obs.:Obrigatório utilizar comando condicional aninhado.

# Utils

def parseNumber(num):
  numero = 0
  try:
    numero = float(num)
  except:
    print("Número inválido! Por favor, digite um número real")
    return 'error'

  return numero    

def gratif(salario):
  if salario < 1000:
    return 200
  elif salario < 1250:
    return 150
  elif salario < 1750:
    return 100
  else:
    return 75

# Main

sbruto = parseNumber(input("Digite o valor do salário bruto: R$ "))

sliquidoPreGratif = sbruto - sbruto*0.11
sliquido = sliquidoPreGratif + gratif(sliquidoPreGratif)

print("O salário liquido é: R$ %.2f" % sliquido)