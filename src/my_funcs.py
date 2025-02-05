# returns the largest value in a list
def get_largest_value_in_list(l):
    largest_value = None

    for e in l:
        if largest_value is None:
            largest_value = e
        elif e > largest_value:
            largest_value = e    
    return largest_value
print(get_largest_value_in_list([15, 2, 3, 4, 5]))