weight = int(input("Weight: "))
unit = input("Write L if your weight is in Lbs, or write K if your weight is in Kg: ")
if unit.upper() == 'L':
    weightConverted = weight * 0.45
    print(f"Your weight in kilos are {weightConverted}")
else:
    weightConverted = weight / 0.45
    print(f"Your weight in pounds are {weightConverted}")