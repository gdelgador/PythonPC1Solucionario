# #### Problema 4

mensaje = 'La suma de los primeros números enteros desde 1 hasta {n} es {suma}'

# 1. ingreso de datos
numero = int(input("Introduce un número entero: "))

# 2. calculo la suma
suma = numero * (numero + 1) / 2

# 3. muestro mensaje
print(mensaje.format(n=numero, suma=suma))