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

# задача6

def number_to_string(num):
 return str(num)

# задача7

def bool_to_word(boolean):
  return "Yes" if boolean else "No"

# задача8

def hero(bullets, dragons): return bullets >= dragons * 2

# задача9

def century(year): return math.ceil(year / 100)

# задача10

def boolean_to_string(b): return str(b)

# Задача11

def past(h, m, s): return (h * 3600 + m * 60 + s) * 1000

# задача12

def double_char(s): return ''.join(char * 2 for char in s)

# задача13

def positive_sum(arr):
 return sum(x for x in arr if x > 0)
