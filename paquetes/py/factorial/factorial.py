def factorial(fact):
 factor = int(1)
 for s in range (1, fact + 1):
     factor = factor * s
 return factor
numero = int(input("ingrese un numero: "))
print("el numero de la factorial es: " + str(factorial(numero)))
      
