
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {1, 2, 3, 4, 5, True, False, 7.8, 8.2, 9.7, 10+4j, 10-4j, 'eleven', 'twelve', 'thirteen'}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = set(range(10, 0, -1))
print(F"s3 :{s3}")
print(type(s3))

print("-" * 40)
s4 = {1, 2, 3}
print(f"s4 :{s4}")

# add new values - add, update
s4.add(3)
s4.add(4)
s4.add(1)
s4.add(5)
s4.add(6)
print(f"s4 :{s4}")

s4.update([3, 4, 5])
s4.update([4, 5, 6])
s4.update([6, 7, 8])
s4.update([1, 2, 3])
s4.update([8, 9, 10])
print(f"s4 :{s4}")

# delete values from a set - pop, remove and discard
print("-" * 40)
print(f"s4 :{s4}")

# pop
res = s4.pop()
print(f"res :{res}")

res = s4.pop()
print(f"res :{res}")

print(f"s4 :{s4}")

print("-" * 40)
# remove

s4.remove(8)
s4.remove(4)
# s4.remove(1)

print(f"s4 :{s4}")

print("-" * 40)
s4.discard(6)
s4.discard(10)
s4.discard(1)

print(f"s4 :{s4}")

print("-" * 40)

A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 40)
print(f"A union B :{A | B}")
print(f"B union A :{B | A}")

print("-" * 40)
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 40)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 40)
print(f"A Symmetric_difference B :{A ^ B}")
print(f"B Symmetric_difference A :{B.symmetric_difference(A)}")

print("-" * 40)
# frozenset = fronzensets are immutable
x = frozenset([1, 2, 3, 4, 5])
print(f"x :{x}")
print(type(x))

