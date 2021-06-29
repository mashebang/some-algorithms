salary = int(input("insira seu salario:"))
percent = int(input("insira o percentual de aumento do salario:"))

total = (salary * (percent / 100)) + salary

print(f'salario inicial: {salary}')
print(f'percentual de aumento: {percent}')
print(f'salario final: {total}')
