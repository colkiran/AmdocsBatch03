
# maketrans and translate
st = 'hello world'
print(f"st :{st}")

a = 'helowrd'
b = 'HELOWRD'
# the lenght of a and b should be the same
resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("translate".center(40, "-"))
res = st.translate(resTbl)
print(f"res :{res}")

print("trim".center(40, "-"))
st = "********hello********"
print(f"st :{st}")

print(st.lstrip("*"))
print(st.rstrip("*"))
print(st.strip("*"))

print("format".center(40, "-"))
print("Welcome {}, what a {} player".format("Messi", "class"))
print("Welcome {} with a rating {}, what a {} player".format("Messi", 9.8456, "class"))
print("Welcome {} with a rating {:.3f}, what a {} player".format("Messi", 9.8456, "class"))

print("Welcome {} with a rating {:.3f}, what a {} player for {}".format("Messi", 9.8456, "class", "Argentina"))

print("Welcome {0} with a rating {1:.3f}, what a {2} player for {3}".format("Messi", 9.8456, "class", "Argentina"))

