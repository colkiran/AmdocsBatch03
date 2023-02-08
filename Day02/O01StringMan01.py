
st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 40)
print(f"st[0] :{st[0]}")            # strings are stored like lists
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

# slicing
print("-" * 40)
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

# reverse indexing
print("-" * 40)
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

# slicing
print("-" * 40)
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

# write a script to find the given string is a palindrome
print("-" * 40)
str1="malayalam"
str2 = str1[::-1]
print("Palindrome" if str1==str2 else "Not Palindrome")

print("-" * 40)
st = "hello world"
print(f"st[0] :{st[0]}")
# st[0] = "H"

# print("-" * 40)
# print(dir(st))

print("find".center(40, "-"))
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1 :{st1}")
print("l :", st1.find("l"))
print("l :", st1.find("l", st1.find("l") + 1))
print("l :", st1.find("l", st1.find("l", st1.find("l") + 1) + 1))

print(f"st2 :{st2}")
print("the :", st2.find("the"))
print("the :", st2.find("the", st2.find("the")+1))

print("replace".center(40, "-"))
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

res = st1.replace("l", "L", 2)
print(f"res :{res}")

res = st2.replace("the", "The", 1)
print(f"res :{res}")
