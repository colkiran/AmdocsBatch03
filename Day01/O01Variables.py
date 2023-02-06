
player_count = 11
team_rating = 4.8
has_won_world_cup = True
team_name = "Shara India"

print(player_count)
print(team_rating)
print(has_won_world_cup)
print(team_name)
# module
print(__name__)         # double underscore => dunder_name

a, b, c = 1, 2, 'hello'
print(a, b, c)

a = b = c = 125
print(a, b, c)

first_name = "Sachin"
last_name = "Tendulkar"

print("My name is " + first_name + " I am also known as " + last_name)

# interpolation => print the value of a variable inside double quotes
# format string or f string

print(f"My name is {first_name} I am also known as {last_name}")

print("-" * 40)
nm1 = "Ooty Apples"
nm2 = "Kanpur Oranges"
print(f"Hello {nm1} and hai {nm2}")

print(f"Today's profit after selling {nm1} and {nm2} is Rs.{15 * 85 + 20 * 120}")

team_name = "Sahara India"
print(team_name)

team_name = "Sahara 'India'"
print(team_name)

team_name = 'Sahara "India"'
print(team_name)

team_name = 'sahara \'India\''
print(team_name)