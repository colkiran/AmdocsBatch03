
l1 = list()
print(F"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.6, 8.1, 9.5, True, False, 12+0j]
print(f'l2 :{l2}')
print(type(l2))

print("-" * 40)
l3 = list(range(10, 101, 10))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l1 = [1, 2, 3, 'four', 'five', 'six']

# memory allocation - id()

print(id(l1[0]))
print(id(l1[1]))
print(id(l1[2]))
print(id(l1[3]))

print("-" * 40)
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l1[3] = 400
print(f"l1 :{l1}")

# print("-" * 40)
# print(dir(l1))

# functions used to add new elements into a list - append, insert and extend

print("append".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
print(l1[8][1:4])

print("extend".center(40, "-"))
l1 = [2, 4, 6, 8, 10]
print(f"L1")

l1.extend([12, 14, 16])
print(f"l1 {l1}")
l1.extend([18, 20, 22])
print(f"l1 :{l1}")

print("Insert".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(F"l1 :{l1}")
l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")
