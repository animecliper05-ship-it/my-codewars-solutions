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

import math
import numbers


def square_sum(numbers):
  return sum(x**2 for x in numbers)


#задача6

def number_to_string(num):
 return str(num)


#задача7

def bool_to_word(boolean):
  return "Yes" if boolean else "No"

#задача8

def hero(bullets, dragons): return bullets >= dragons * 2

# задача9

def century(year): return math.ceil(year / 100)


# задача10

def boolean_to_string(b): return str(b)

# Задача11

def past(h, m, s): return (h * 3600 + m * 60 + s) * 1000

# задача12

def double_char(s): return ''.join(char * 2 for char in s)

#задача13

def positive_sum(arr):
 return sum(x for x in arr if x > 0)

# задача14

def maps(a): return [x * 2 for x in a]

# задача15

def remove_char(s): return s[1:-1]

#задача16

def make_upper_case(s): return s.upper()

# задача17

def remove_exclamation_marks(s): return s.replace('!', '')

# задача18

def enough(cap, on, wait): return max(0, on + wait - cap)

#задача19

def invert(lst): return [-x for x in lst]

#задача20

def hoop_count(n: int) -> str: return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"

#задача21

def get_grade(s1: int, s2: int, s3: int) -> str:
    score = (s1 + s2 + s3) / 3

    if score >= 90: 
        return 'A'
    if score >= 80: 
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60: 
        return 'D' 
    return 'F'


# задача22

def feast(beast: str, dish: str) -> bool: return beast[0] == dish[0] and beast[-1] == dish[-1]

#задача23

def is_even(n: float) -> bool: return n % 2 == 0

 # задача24

def get_age(age_str: str) -> int: return int(age_str[0])

#задача25

def bmi(weight: float, height: float) -> str:
    bmi_value = weight / (height ** 2)
    
    if bmi_value <= 18.5: 
        return "Underweight"
    if bmi_value <= 25.0: 
        return "Normal"
    if bmi_value <= 30.0: 
        return "Overweight"
    return "Obese"

#задача26

def get_volume_of_cuboid(length: float, width: float, height: float) -> float: return length * width * height

# задача27

def human_years_cat_years_dog_years(human_years: int) -> list:
    if human_years == 1: 
        return [1, 15, 15] 
    if human_years == 2: 
        return [2, 24, 24]
        
    cat_years = 24 + (human_years - 2) * 4
    dog_years = 24 + (human_years - 2) * 5
    return [human_years, cat_years, dog_years]

# задача28 

def even_or_odd(number: int) -> str: return "Even" if number % 2 == 0 else "Odd"

# задача 29

def greet(name: str) -> str: return f"Hello, {name} how are you doing today?"

# задача 30

def sum_array(arr):
   if not arr or len(arr) <= 2:
    return 0
    return sum(arr) - min(arr) - max(arr)

## задача 31

DATABASE = { "english": "Welcome", "czech": "Vitejte", "danish": "Velkomst", "dutch": "Welkom", "estonian": "Tere tulemast", "finnish": "Tervetuloa", "flemish": "Welgekomen", "french": "Bienvenue", "german": "Willkommen", "irish": "Failte", "italian": "Benvenuto", "latvian": "Gaidits", "lithuanian": "Laukiamas", "polish": "Witamy", "spanish": "Bienvenido", "swedish": "Valkommen", "welsh": "Croeso" }

def greet(language: str) -> str: return DATABASE.get(language, "Welcome")

# задача 32

def simple_multiplication(number: int) -> int: return number * 8 if number % 2 == 0 else number * 9

#задача 33

def string_to_number(s: str) -> int:
 return int(s)

# задача 34

def goals(la_liga: int, copa_del_rey: int, champions: int) -> int: return la_liga + copa_del_rey + champions

#задача 35

def repeat_str(repeat: int, string: str) -> str:
  return string * repeat