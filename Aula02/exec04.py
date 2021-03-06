# Escreva um programa em Python que calcule as duas raízes de uma equação de 2º grau ax²+bx+c, conhecendo os valores dos coeficientes da mesma (a, b, c). Suponha que as raízes são reais. Lembre-se que para calcular as duas raízes

a = float(input("Informe o valor de A "))
b = float(input("Informe o valor de B "))
c = float(input("Informe o valor de C "))
d = (b**2) - 4*a*c

print("as raizes são: ", str((-b+(d**(1/2)))/2*a), "e ", str((-b-(d**(1/2)))/2*a))