# #### Problema 8

respuesta = input("Qué hora es? ")
respuesta = respuesta.lower().strip()

hora, minuto = respuesta.split(':')

h = float(hora) + int(minuto)/60

if 7<= h <= 8:
    print('breakfast time')
elif 12<= h <= 13:
    print('lunch time')
elif 18<= h <= 19:
    print('dinner time')
    