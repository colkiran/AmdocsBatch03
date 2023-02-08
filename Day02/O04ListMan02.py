
# functions used to delete elements of a list - pop, remove, clear

print("pop".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(1)
print(f"res :{res}")

res = l1.pop()
print(f"res :{res}")

# res = l1.pop(9)
# print(f"res :{res}")

print(f"L1 :{l1}")

print("remove".center(40, "-"))
l1 = [1, 2, 2, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]

print(f"l1 :{l1}")

l1.remove(3)
l1.remove(3)
# l1.remove(3)

print(f"l1 :{l1}")

# write a code to remove all 1's from the list
print("-" * 40)

# while l1.count(1):
#     l1.remove(1)

# print(f"l1 :{l1}")

res  = [x for x in l1 if x != 1]            # list comprehension
print(res)


print("-" * 40)
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print('index'.center(40, "-"))
l1 = [1, 2, 1, 1, 1, 2, 3, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 2, 1, 2, 1, 1, 2, 3, 1, 1, 1, 1]
print(f"l1 :{l1}")

print("3 :",  l1.index(3))
print("3 :",  l1.index(3, l1.index(3)+1))
print("3 :",  l1.index(3, l1.index(3, l1.index(3)+1)+1))

