weight = float(input("Vikt: "))
while weight < 20.0 or weight > 300.0:
    print("fel, måste vara mellan 20 och 300")
    weight = float(input("vikt: "))
height = float(input("Längd: "))
while height < 1.0 or height > 2.5:
    print("fel, måste vara mellan 1 och 2.5")
    height = float(input("längd: "))
bmi = weight/ height ** 2

print("BMI: ", bmi)
print("Viktklass: ", end = " ")
if bmi < 18.5:
    print("Underviktig")
elif bmi < 25.0:
    print("normalvikt")
elif bmi < 30.0:
    print("överviktig")
else:
    print("fetma")
