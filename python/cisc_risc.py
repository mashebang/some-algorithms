""""
risc - reduced instruction set Computers
cisc - complex instruction set Computers

## aplicacoes
## linguagens de programacao
## sistema operacional
## hardware

"""




import math

##

# risc - reduced instruction set instruction
class Risc:
  def add(self, a, b):
    return a + b

  def minus(self, a, b):
    return a - b

# cisc - complex instruction set instruction

class Cisc:
  def add(self, a, b):
    return a + b

  def minus(self, a, b):
    return a - b

  def divide(self, a, b):
    return a / b

  def multiply(self, a, b):
    return a * b

  def square_root(self, a):
    return math.sqrt(a)

  def power(self, a, b):
    return pow(a, b)


## exemplos
a = 2
b = 3
cisc_so = Cisc()
risc_so = Risc()


# SOMA 
print(cisc_so.add(a, b))
print(risc_so.add(a, b))

# MULTIPLICACAO

print(cisc_so.multiply(a, b))

risc_multiply_value = 0

for i in range(0, a):
  risc_multiply_value = risc_so.add(risc_multiply_value, b)

print(risc_multiply_value)

