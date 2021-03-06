# Escreva um programa em Python que leia a cotação do dólar (taxa de conversão), leia um valor em dólares e converta e mostre o valor equivalente em Reais.

cotDol = float(input("Informe a cotação do dolar "))
dol = float(input("Informe a quantidade em dolar "))

brl = cotDol*dol

print(str(dol), "USD é equivalente a : ", "%.2f" % brl,"BRL")