
cities = ['thiruvananthapuram', 'bangalore', 'delhi', 'hyderabad', 'pune', 'mumbai', 'kolkota', 'chennai' ]

print(cities)

# sort these names by thier length

print('-' * 40)

res = sorted(cities, key=len)

print(res)
