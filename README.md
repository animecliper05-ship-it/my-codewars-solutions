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

# Задача 14. Принимает список чисел и возвращает новый список, где каждое число умножено на 2.

def maps(a): return [x * 2 for x in a]

# Задача 15. Удаляет первый и последний символы из переданной строки.

def remove_char(s): return s[1:-1]

# Задача 16. Переводит все буквы в строке в верхний регистр (заглавные).

def make_upper_case(s): return s.upper()

# Задача 17. Удаляет все восклицательные знаки из переданной строки.

def remove_exclamation_marks(s): return s.replace('!', '')

# Задача 18. Считает, сколько пассажиров не поместится в автобус исходя из вместимости, занятых мест и очереди.

def enough(cap, on, wait): return max(0, on + wait - cap)

# Задача 19. Меняет знак каждого числа в списке на противоположный (положительные на отрицательные и наоборот).

def invert(lst): return [-x for x in lst]

# Задача 20. Проверяет количество оборотов обруча и возвращает мотивационное сообщение (порог — 10 раз).

def hoop_count(n: int) -> str: return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"

# Задача 21. Вычисляет среднее арифметическое трёх оценок и возвращает итоговую буквенную оценку (A, B, C, D или F).

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

# Задача 22. Проверяет, совпадают ли первая и последняя буквы в названии животного и блюда.

def feast(beast: str, dish: str) -> bool: return beast[0] == dish[0] and beast[-1] == dish[-1]
