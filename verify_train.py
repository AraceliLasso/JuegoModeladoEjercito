from models.unit import Unit
from models.army import Army
import time

army = Army("chinese", "Ejército Chino")

unit1 = army.units[0]

print(f"Creating unit, Type: {unit1.unit_type}")
print(f"[{unit1.unit_type.capitalize()}] Initial strength: {unit1.get_strength()}")
print(f"Army gold before training: {army.gold}")

try:
    army.train_unit(unit1)
    print(f"[{unit1.unit_type.capitalize()}] Strength after training: {unit1.get_strength()}")
    print(f"Army gold after training: {army.gold}")
except ValueError as e:
    print(f"Training failed: {e}")

if unit1.can_transform():
    print(f"[{unit1.unit_type.capitalize()}] Transformation available.")
    print(f"Army gold before transformation: {army.gold}")
    try:
        army.transform_unit(unit1)
        print(f"Unit transformed into: {unit1.unit_type}")
        print(f"[{unit1.unit_type.capitalize()}] Strength after transformation: {unit1.get_strength()}")
        print(f"Army gold after transformation: {army.gold}")
    except ValueError as e:
        print(f"Transformation failed: {e}")
else:
    print(f"[{unit1.unit_type.capitalize()}] Cannot be transformed.")

print(f"[{unit1.unit_type.capitalize()}] Years lived: {unit1.get_years_lived()}")

