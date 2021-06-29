# -*- coding: utf-8 -*-
a = int(input("insira o valor de a: "))
b = int(input("insira o valor de b: "))

def getFunctionEvolution(a):
	if a > 0:
		return 'crescente'
	else:
		return 'decrescente'

def getFunctionZero(a, b):
	return (b * -1) / a

def getSignalIntervals(a, b):
	evolution = getFunctionEvolution(a)
	zero = getFunctionZero(a, b)

	first_rule = "maior" if evolution == "crescente" else "menor"
	second_rule = "menor" if evolution == "crescente" else "maior"

	return f'A função é positiva sempre que X {first_rule} que {zero} e negativa sempre que X {second_rule} que {zero}'


print(f'a funcao eh {getFunctionEvolution(a)} \n')
print(f'o zero da funcao eh: {getFunctionZero(a, b)} \n')
print(getSignalIntervals(a, b))
