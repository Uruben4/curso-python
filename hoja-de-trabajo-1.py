#ejercicio 1

def my_funcion(color):
    if color == 'naranja':
        print('has ganado')
    else: 
        print('has perdido')

my_funcion(input('Cual es el color de la fruta? '))

#ejercicio 2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return (fibonacci(n - 1) + fibonacci(n - 2))
    
i = int(input('Ingrese un numero: '))
item = fibonacci(i)
print('el resultado de la serie es: ', item)

#Ejercicio 3 

def factorial(numero):
    if numero == 0: 
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input('Ingrese un numero: '))
resultado = factorial(numero)
print('el resultado de la serie es: ',resultado) 
        


















    

