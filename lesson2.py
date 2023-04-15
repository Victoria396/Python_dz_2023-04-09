import collections

def homeTask1():
    n = int(input('введите число:'))
    fact = 1
    list = []

    for i in range(1, n+1):
        fact *= i
        list.append(fact)

    print(list)

# homeTask1()

# Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
def homeTask2():
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f'{x} | {y} | {z} | {int(not(x and y) or z)}')

# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается 
# во второй «one» «onetwonine» - o – 2, n – 3, e – 2
def homeTask3():
    string = input('Введите строку: ')
    string_for_compare = input('Введите строку для сравнения: ')

    letter_string = collections.defaultdict(int)
    letter_string2 = collections.defaultdict(int)
    for letter in string:
        letter_string[letter] += 1
    print(letter_string)

    for letter in string_for_compare:
        letter_string2[letter] += 1
    print(letter_string2)
    
    # print(int(set(letter_string) & set(letter_string2)))
    print([i for i, j in zip(letter_string, letter_string2) if i == j])

def homeTask4():
    numbers = []
    n = int(input('введите число: '))
    list1 = []
    for el in range(-n, n+1):
        list1.append(el)
    
    numbers = list1[-2:] + list1[:-2]
    print(numbers)

homeTask1()
homeTask2()
homeTask3()
homeTask4()
