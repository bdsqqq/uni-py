# Questão1 (0,75 pts) -Faça um programa em Pythonque calcule o valor em Dólares ($), correspondente ao valor em Reais (R$) que um turista possui no cofre do hotel. O programa deve solicitar os seguintes dados: quantidade de reais guardados no cofre e cotação do dólar no dia. Calcule e mostre o valor calculado.

# Utils

def parseNumber(num):
  numero = 0
  try:
    numero = float(num)
  except:
    print("Número inválido! Por favor, digite um número real")
    return 'error'

  return numero

# Main

dindinNoCofre = parseNumber(input("Quantos reais estão guardados no cofre? R$ "))
cotacaoDol = parseNumber(input("Qual a cotação atual do dolar? R$ 1.00 = USD "))

dindinEmDol = dindinNoCofre * cotacaoDol

print("O valor valor do dinheiro guardado no cofre, em dolar, é: USD %.2f" % (dindinEmDol))