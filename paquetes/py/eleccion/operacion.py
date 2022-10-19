def elegirnum():
    global num1, num2
    num1 =int(input("digite el primer numero: "))
    num2 =int(input("digite el segundo numero: "))
    
def sumar (s, d):
    print("la suma ",s," + ",d," = ",s+d)
def resta (s, d):
    print("la suma ",s," - ",d," = ",s-d)
def multiplicacion (s, d):
    print("la suma ",s," * ",d," = ",s*d)
def sumar (s, d):
    if d == 0:
        print("no  es posible dividir entre cero")
    else:
        print("la division" ,a," / ",b," = ",a/b)
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
    print("la factorial es")
    
    print("""cual operacion nesecita:
           1.suma
           2.resta
           3.multiplicacion
           4.divicion
           5.factorial
           6.salir
           """)
    eleccion = int(input())

    if eleccion == 1:
        elegirnum()
        sumar(num1, num2)
    elif eleccion == 2:
        elegirnum()
        resta(num1, num2)
    elif eleccion == 3:
        elegirnum()
        multiplicacion(num1, num2)
    elif eleccion == 4:
        elegirnum()
        division(num1, num2)
    elif eleccion == 5:
        elegirnum()
        factorial(num1, num2)
    elif eleccion ==6:
        print("salir")
        

        
