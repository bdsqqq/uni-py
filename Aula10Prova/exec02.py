# Questão 2 (1,0) -Faça um programa em Python que solicite ao usuário o valor do raio de uma esfera:
#a)Calcule e mostre o seu comprimento(formatado com 2casas decimais), sabendo que: C = 2 * pi* raio
# b) Calcule e mostre o seu volume(formatado com 2casas decimais), sabendo que: V = 4/3* pi * raio^3
# Obs.:A  fórmula  deve  ser  construída  respeitando  a  precedência  dos  operadores  aritméticos  e  utilizando  as  funções matemáticas (obrigatório utilizar o módulo matemático).

import math 

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

raio = parseNumber(input("Digite o valor do raio de uma esfera: "))

comprimento = 2 * math.pi * raio
volume = (4/3) * math.pi * math.pow(raio, 3)

print("Considerando uma esfera de raio %.2f" % raio)
print("a) O comprimento é: %.2f" % comprimento)
print("b) O volume é: %.2f" % volume)