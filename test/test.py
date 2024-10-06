import sys
sys.path.append("/Users/guliamova/sudo_test/build")

import sign_module

db = sign_module.SignDatabase()

sign1 = sign_module.Sign("Stop", 1, sign_module.Coordinates(37.6173, 55.7558))

db.add_sign(sign1)

try:
    db.add_sign(sign1)
except RuntimeError as e:
    print(f"Expected exception caught: {e}")

found_sign = db.find_sign(1)
print(f"Found sign: {found_sign.name}, ID: {found_sign.id}, Coordinates: ({found_sign.coordinates.longitude}, {found_sign.coordinates.latitude})")

try:
    db.find_sign(100)
except RuntimeError as e:
    print(f"Expected exception caught: {e}")

db.remove_sign(1)
print("Sign with ID 1 removed successfully.")

db.remove_sign(100)  
print("Attempted to remove non-existing sign (ID 100).")

sign2 = sign_module.Sign("Yield", 2, sign_module.Coordinates(40.7128, -74.0060))
sign3 = sign_module.Sign("No Entry", 3, sign_module.Coordinates(48.8566, 2.3522))

db.add_multiple_signs([sign2, sign3])

found_sign2 = db.find_sign(2)
print(f"Found sign 2: {found_sign2.name}")

found_sign3 = db.find_sign(3)
print(f"Found sign 3: {found_sign3.name}")

try:
    db.add_multiple_signs([sign2, sign1])
except RuntimeError as e:
    print(f"Expected exception when adding duplicate signs: {e}")

max_id_sign = sign_module.Sign("Max ID Sign", 2**32-1, sign_module.Coordinates(10.0, 10.0))
db.add_sign(max_id_sign)
print(f"Added sign with max ID: {max_id_sign.id}")

found_max_sign = db.find_sign(2**32-1)
print(f"Found sign with max ID: {found_max_sign.name}")

db.remove_sign(2**32-1)
print(f"Sign with max ID removed")
