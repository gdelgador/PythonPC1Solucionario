# #### Problema 3

PESO_PAYASOS = 112
PESO_MUNECAS = 75

# ingreso datos
cantidad_payasos = int(input("Introduce el número de payasos a enviar: "))
cantidad_munecas = int(input("Introduce el número de muñecas a enviar: "))

# calculo y resultado
peso_total = PESO_PAYASOS * cantidad_payasos + PESO_MUNECAS * cantidad_munecas
print("El peso total del paquete es {}".format(peso_total))

