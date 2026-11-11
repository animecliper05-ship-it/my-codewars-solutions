# задача1 

def reverse_seq(n): return list(range(n, 0, -1))

# задача2 

def are_you_playing_banjo(name):
    if name[0].lower() == 'r': 
        return name + " plays banjo" 
    else: 
        return name + " does not play banjo"


# задача3

def abbrev_name(name): return '.'.join(word[0].upper() for word in name.split(' '))

# задача4

def zero_fuel(distance_to_pump, mpg, fuel_left): return fuel_left * mpg >= distance_to_pump

# задача5

def square_sum(numbers):
  return sum(x**2 for x in numbers)
