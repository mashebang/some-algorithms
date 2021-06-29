import math
area = float(input("insira a area em metros quadrados a ser pintada: "))
metersByCan = 18 * 3
canValue = 150

if (area < metersByCans):
	print('1 lata sera necessaria.')
	print(f'valor total: {canValue}')
else:
	totalCans = math.ceil(area / metersByCan)
	totalValue = totalCans * canValue
	print(f'{totalCans} lata(s) sera(ao) necessaria(s).')
	print(f'valor total: {totalValue}')
