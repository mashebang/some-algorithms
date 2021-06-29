def planA(minutes):
	return 30 + minutes

def planB(minutes):
	return 20 + (1.5 * minutes)


def planC(minutes):
	return 3 * minutes

userMinutes = int(input("Quantos minutos você pretende usar por mês?"))

plan = {
	"name": "A",
	"value": planA(userMinutes)
}

testValue = planB(userMinutes)

if (plan['value'] > testValue):
	plan = {
		"name": "B",
		"value": planB(userMinutes)
	}


testValue = planC(userMinutes)

if (plan['value'] > testValue):
	plan = {
		"name": "C",
		"value": testValue
	}

print(f'para {userMinutes} minutos, a melhor escolha é o plano {plan["name"]}, custando: R$ {plan["value"]:.2f}')
