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
        
def funcion():
    n = int(input('Ingrese un numero: '))
    w1 = 1
    w2 = 2
    s = 0
    c = 0
    if n <= 0:
        print('error')
    elif n == 1:
        print(w1)
    else:
        while c < n:
            print(w1)
            s = w1 + w2
            w1 = w2
            w2 = s
            c += 1
funcion()


















    

