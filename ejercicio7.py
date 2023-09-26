# #### Problema 7

MSG = """Elija una de las siguientes opciones:

a) Mostrar la suma de los dos números
b) Mostrar la resta de los dos números (el primero menos el segundo)
c) Mostrar la multiplicación de los dos números
"""

# Solicito datos
x = int(input('Ingrese su primer número: '))
y = int(input('Ingrese su segundo número: '))


# menu inicio
print(MSG)

# De acuerdo respuesta, realizamos operacion
respuesta = input('Ingrese una de las 3 opciones (a, b ó c): ') 
respuesta= respuesta.lower()

if respuesta == 'a' :
    suma = x + y
    print(f'Suma = {suma}')
elif respuesta == 'b' :
    resta = x - y
    print(f'Resta = {resta}')
elif respuesta == 'c' :
    multiplicacion = x * y
    print(f'Multiplicación = {multiplicacion}')
else:
    print('¡Incorrecto! Opción inválida')