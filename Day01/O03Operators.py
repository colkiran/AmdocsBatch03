
"""
Arithmetic Operators
Logical Operator
Comparison Operator
Bitwise Operator
Augmentor Operator
Ternary Operator
"""

print(f"Add :10 + 3 = {10 + 3}")
print(f"Sub :10 - 3 = {10 - 3}")
print(f"Mul :10 * 3 = {10 * 3}")
print(f"Div :10 / 3 = {10 / 3}")
print(f"Floor :10 // 3 = {10 // 3}")        # 10 // 3 = 3
print(f"Mod :10 % 3 = {10 % 3}")
print(f"Exp :10 ** 3 = {10 ** 3}")

print("Augmentor".center(40, "-"))
# =, +=, *=, -=, /=
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison Operator".center(40, "-"))
# ==, >, >=, <, <=, !=
a = 10
b = 12
print(f"a :{a}")
print(f"b :{b}")

print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("Logical Operators".center(40, "-"))
# and, or, not
print(1 == 1 and 2 == 2)
print(1 == 2 and 2 == 2)

print(1 == 2 or 2 == 1)
print(1 == 1 or 2 == 1)

print(not(1 == 2 or 2 == 1))
print(not(1 == 1 or 2 == 1))

print("-" * 40)
print(f"ord('A') :{ord('A')}")      # integer representation of unicode characters
print(f"ord('Z') :{ord('Z')}")
print(f"ord('a') :{ord('a')}")
print(f"ord('z') :{ord('z')}")
print("apple" > "orange")
print("apple" < "orange")

print("Bitwise Operators".center(40, "-"))
print(f"5 | 3 :{5 | 3}")
print(f'5 & 3 :{5 & 3}')
print(f'5 ^ 3 :{5 ^ 3}')
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1: {16 >> 1}")
print(f"5 >> 1: {5 >> 1}")

# ternary Operator
a = 26
print("Eligible" if a >= 18 else "Not Eligible")
