# #### Problema 2

costo = float(input("Cuanto costo la comida? "))
propina = float(input("Qué porcentaje de propina desea dejar? "))

tip = costo * propina /100
print(f"Propina ${tip:.2f}")
