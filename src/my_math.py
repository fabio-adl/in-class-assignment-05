
# Sums 2 different numbers
def sum(a,b):
    return a + b

# Multiplies 2 different numbers
def multiply(a,b):
    return a * b

# Subtract 2 different numbers
def difference(a,b):
    return a - b

# Adds 2 numbers, but the result is always positive
# for example -10 + 5 = 15
# this code can be made simpler with some refactoring
def absolute_sum(a,b):
    if a < 0 or b < 0:
        return abs(a) + abs(b)
    else:
        return a + b

print(absolute_sum(-1,1))

# Calculates birth year with a current year and an age
# takes into account if the birthday has already occurred
def calculate_birth_year(current_year, age, had_birthday_in_current_year):
    birth_year = current_year - age
    if not had_birthday_in_current_year:
        return birth_year - 1
    return birth_year

print(calculate_birth_year(2025, 43, False))