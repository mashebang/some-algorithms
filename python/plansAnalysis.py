def planA(minutes):
	return 30 + minutes

def planB(minutes):
	return 20 + (1.5 * minutes)


def planC(minutes):
	return 3 * minutes

plan = {
	"name": "",
	"value": 0
}

for i in range(100):
	plan = {
		"name": "A",
		"value": planA(i)
	}

	testValue = planB(i)

	if (plan['value'] > testValue):
		plan = {
			"name": "B",
			"value": planB(i)
		}


	testValue = planC(i)

	if (plan['value'] > testValue):
		plan = {
			"name": "C",
			"value": testValue
		}

	print(f'para {i} minutos, a melhor escolha é o plano {plan["name"]}, custando: R$ {plan["value"]:.2f}')
