length = int(input("Zadejte délku v milimetrech: "))
lenght_cm = length / 10
length_m = length / 1000
lenght_inch = length / 25.4
print(f"Přeovody: {length} mm = {lenght_cm:.3f} cm = {length_m:.3f} m = {lenght_inch:.3f} inch")