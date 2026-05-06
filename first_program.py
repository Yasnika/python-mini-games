
##a = [1, 2, 3] * 5
##print(a)
##a.remove(3)
##print(a)
##while 3 in a:
 ##   a.remove(3)
 ##   print(a)  

##s = 'qwertyu@#!iOPAsdfghjkxcvbnm'
##while len(s) > 0:
  ##  bukva = s[0]
    ##if bukva >= 'a' and bukva <= 'z':
      ##  print(bukva, 'small')
    ##elif bukva >= 'A' and bukva <= 'Z':
      ##  print(bukva, 'big')
    ##elif bukva.isdigit():
      ##  print(bukva, 'digit')
    ##else:
      ##  print(bukva, 'znak')
        
    ##s = s[1:]


##i = 0
##while i < 101:
##    print(i)
##    i += 1

##n = int(input())
##i = 1
##while i < n + 1:


                                 # break and continue
#for i in range(1, 101):
#    if i == 7 or i == 17 or i == 29 or i == 78:
#        continue  # переходит на следующую итерацию
#    print(i)

#i = 100
#while i > 0:
#    if i == 40:
#        break
#    print(i, end='*')
#    i -= 20

#i = 1
#while True:
#    print('итерация №', i)
#    if i == 10:
#        break
#        print('hi')
#    i += 1
#print('hello')

#while True:
#    a = input()
#    if a == 'exit':
#        break
#    if len(a) < 5:
#        continue
#    print(a, len(a))

#n = 5 
#while n > 0:
#    n -= 1
#    print(n)
#else:
#    print('Цикл завершен')

#for hours in range(24):
#    for minutes in range(60):
#        for seconds in range(60):
#           print(hours, ':', minutes, ':', seconds)


#cnt = 0
#total = 0
#for i in range(1, 10):
#    num = int()    
#    cnt += 1
#    total += num 
#    kk = total / cnt 
#print(kk)

#a = int('1')
#b = int('2')
#c = int('3')
#d = int('4')
#e = int('5')
#f = int('6')
#g = int('7')
#h = int('8')
#i = int('9')
#kk = a + b + c + d + e + f + g + h + i 
#tt = kk / 9
#print(tt)

#a = int('8')
#b = int('11')
#tt = min(a, b)
#print(tt)

#a = int('8')
#b = int('11')
#if a > b:
#    print(a > b)
#elif a == b:
#    print(a = b)
#else:
#    print(a)

#total = 0
#for x in range(1, 65):
#  for y in range(1, 60):                   # решение уравнении 12x + 13y = 777
#    if 12 * x + 13 * y == 777:
#      total += 1
#      print('x=', x, 'y=', y)
#print(total)

#for n in range(1, 13):
#    for k in range(1, 12):
#        for m in range(1, 12):
#            if 28 * n + 30 * k + 31 * m == 365:
#                print(n, k, m)


                
#total = 0
#for n in range(1, 101):
#    for k in range(1, 101):
#        for m in range(1, 101):
#            if 10 * n + 5 * k + 0.5 * m == 100 and n + k + m == 100:
#                total += 1
#                print('n=', n, 'k=', k, 'm=', m)
#print(total)

#for a in range(1, 151):
#    for b in range(a, 151):
#        for c in range(b, 151):
#            for d in range(c, 151):
#                for e in range(d, 151):
#                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e  ** 5:                        
#                        print(a, b, c, d, e)
#                        print(a + b + c + d + e)
#                        break     


                    
#for a in range(1, 33):
#    for c in range(1, a):
#        for d in range(1, c):
#            for b in range(1, d):
#                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
#                    print(a ** 3 + b ** 3)               

# s = '01234567891011121314151617'
#for i in range(0, len(s), 5):
#    print(s[i], end='')ОГТ


'''a = 'I'
b = 'will'
c = 'be'
d = 'back'
a, b, c, d = ord(a), ord(b), ord(c), ord(d)
maxx = max(a, b, c, d)
print(maxx)'''

'''numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num, end=' ')'''

'''numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*numbers, sep='\n')'''

'''n = [8, 9, 10, 11]
del n[1]
n.insert(1, 17)
print(n)  # norm
n.append(4)
n.append(5)
n.append(6)
print(n)  # ?
n.remove(n[0])
print(n)
print(n * 2)
n.insert(3, 25)
print(n)
print(n)'''

'''numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.append(4)
numbers.append(5)
numbers.append(6)
del numbers[0]
copy = numbers.copy()
numbers.extend(copy)
numbers.insert(3, 25)
print(numbers)'''

'''numbers = ['10', '5', '9', '1', '11']
numbers.sort()

print(numbers)'''

'''words = ['aunt', 'Anton', 'Anna', 'a', 'an']
words.sort()

print(words)'''

'''numbers = []

for i in range(1, 5):
    for j in range(2):
        numbers.append(i * j)
print(numbers)'''

'''expression = '5 + 5 * 2 = 15'
digits = [int(c) for c in expression if c.isdigit()]

print(digits)'''


'''keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [i[1:] for i in keywords]
print(new_keywords)'''

'''keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [len(i) for i in keywords]

print(lengths)'''

'''keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [keywords[i] for i in range(len(keywords)) if i <= 5]

print(new_keywords)'''

'''palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]

print(palindromes)'''

'''n = int(5)
s = [i ** 2 for i in range(1, n + 1)]
print(*s, sep='\n') '''

'''a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
            a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами 

print('Отсортированный список:', a)'''

'''a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

n = len(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)'''

'''a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)
            

# реализация алгоритма сортировки выбором

print(sorted(a))'''


'''def convert_grade(grade):
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70: 
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1

# основная программа
grade = int(input('Введите вашу отметку по 100-балльной системе: '))
print(convert_grade(grade))'''

'''def sep_a(tii):
    a = tii + 6 ** 2
tii = float(input())
sep_a(tii)
result tii'''

'''num = 4
while num < 10:
    num += 2
    print(num)
else:
    print('Цикл завершен.')'''

'''num = 1964
while num != 0:
    last_digit = num % 10
    num //= 10

    if last_digit % 3 == 0:
        print(last_digit)
        break  '''

'''def draw_triangle():
    height = 8
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)   
        
# основная программа
draw_triangle()  # вызов функции  '''

                                                     # Мой первый калькулятор)) 08.02.26г.
'''def coco_do():
    a = float(input('Введите первое число: '))
    operator = input('Введите опетатора (/, *, +, -): ')
    b = float(input('Введите второе число: '))
    
    if operator == '*':
        print(a * b)
    elif operator == '/':
        print(a / b)
    elif operator == '+':
        print(a + b)
    elif operator == '-':
        print(a - b)
    else:
        print('Ошибка ввода!') 

coco_do()'''
                                       # мой мини код))) 26.02.26
'''n = int(input())
if n != 2 and n != 7 and n % 2 != 1:
    print((n + 9) % 2)
else:
    print('Вы ввели неправильное число!')'''
    

'''total = 1
while total < 10:
    num = int(input())
    total *= num
    print(total)    '''

'''for i in range(2):
    for j in range(2):
        print('*', end='#')

    for k in range(3):
        print('%', end='&')

    print()'''

'''numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
s = 0
for i in range(len(numbers)):
    s += numbers[i] ** 2
print(s)'''

'''keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [keywords[i][1:] for i in range(len(keywords))]

print(new_keywords)'''

'''n = [i ** 2 for i in range(1, int(input()) + 1)]
print(n)'''


                                    #1 Числовая угадайка  26/04/26

'''import random 
num = random.randint(1,100)
print('Угадайте число от 1 до 100')
while True:
    n = int(input('введите число:'))
    if n > num:               
        print('Слишком много, попробуйте еще раз')           
    elif n < num:  
        print('Слишком мало, попробуйте еще раз')                  
    elif n == num:
        print('Вы угадали, поздравляем!')  
        break'''

                                 #2 Числовая угадайка 28.04.26
'''print('Добро пожаловать в числовую угадайку!')
import random 
num = random.randint(0, 100)
cnt = 0
while True:
    n = int(input('Введите число от 0 до 100: '))
    if num > n:
        print('Ваше число меньше загаданного')
    elif num < n:
        print('Ваше число больше загаданного')
    elif num == n:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')   
        break
    cnt += 1
    print('Количество попыток:', cnt)
        
game = input('Сыграем еще разок? (д/н): ')
if game == 'н':
    print('Возвращайтесь скорее!')'''

                                    # Магический шар 8 !
'''import random 

answers = ['Бесспорно','Предрешено','Никаких сомнений','Определенно да','Можешь быть уверен в этом','Мне кажется - да','Вероятнее всего','Хорошие перспективы','Знаки говорят - да','Да','Пока неясно, попробуй снова','Спроси позже','Лучше не рассказывать','Сейчас нельзя предсказать','Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут?')
print('Привет', name)
while True:
    question = input('Задавай любой вопрос:')
    ran = random.choice(answers)
    print('Ответ:', ran)

    n = input('Хочешь задать еще вопрос? (д/н)')
    if n == 'д':
        print('Продолжаем!')
    else:
        print('Возвращайся, если возникнут вопросы!')
        break'''

                                         # Магический шар 8   29/04/26
'''# Заголовок программы
import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

#Считывание пользовательских данных
a = int(input('Сколько паролей необходимо?'))
b = int(input('Какой длинны вам нужен пароль?'))
iskl = 'il1Lo0O'

if input('Включать ли цифры 0123456789? (да или нет)').lower() == 'да':
    chars += digits      
if input('Включать ли строчные буквы a-z? (да или нет)').lower() == 'да':
    chars += lowercase_letters 
if input('Включать ли прописные буквы A-Z? (да илинет)').lower() == 'да':
    chars += uppercase_letters 
if input('Включать ли символы "!#$%&*+-=?@^_" ? (да или нет)').lower() == 'да':
    chars += punctuation
if input('Исключать ли неодназначные символы "il1Lo0O" ? (да или нет)').lower() == 'да':
    for i in iskl:
        chars = chars.replace(i, '')

# Генерация пароля
def generate_password(a, b, chars):        
    if chars == '':
        print('Вы не выбрали ни одного набора символов!')
        return
    
    for i in range(1, a + 1):
        password = ''.join(random.choices(chars, k = b))
        print(f'{i}. {password}')

generate_password(a, b, chars)      '''



                                        # Шифр Цезар 30.04.26
'''print('Добро пожаловать!')
def shifr_ie():
    a = input('Что вы выберите шифрование(+) или дешифрование(-) ?').lower()
    b = input('На каком языке ? (русский или английский)').lower()
    c = int(input('Выберите шаг сдвига (со сдвигом вправо)'))
    d = input(f'Введите текст который хотите {a}: ')

    if b == 'русский':
        upper_alph = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        lower_alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    elif b == 'английский':
        upper_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_alph = 'abcdefghijklmnopqrstuvwxyz'
    else:
        print('Неверный язык!')
        return

    if a == '+':
        print(shifr_ie_2(d, c, upper_alph, lower_alph))
    elif a == '-':
        print(shifr_ie_3(d, c, upper_alph, lower_alph))
    else:
        print('Неверный режим!')

def shifr_ie_2(d, c, upper_alph, lower_alph):
    text = ''
    for char in d:
        if char in upper_alph:
           new = (upper_alph.index(char) + c) % len(upper_alph)
           text += upper_alph[new]
        elif char in lower_alph:
            new = (lower_alph.index(char) + c) % len(lower_alph)
            text += lower_alph[new]
        else:
            text += char # пробелы, цифры и т.д.
    return text

def shifr_ie_3(d, c, upper_alph, lower_alph):
    txt = ''
    for char in d:
        if char in upper_alph:
           new = (upper_alph.index(char) - c) % len(upper_alph)
           txt += upper_alph[new]
        elif char in lower_alph:
            new = (lower_alph.index(char) - c) % len(lower_alph)
            txt += lower_alph[new]
        else:
            txt += char # пробелы, цифры и т.д.
    return txt
           
shifr_ie()'''

'''text = 'Блажен, кто верует, тепло ему на свете!'
c = int(10)
upper_a= 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_a = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
txt = ''

for char in text:
    if char in upper_a:
        new = (upper_a.index(char) + c) % len(upper_a)
        txt += upper_a[new]
    elif char in lower_a:
        new = (lower_a.index(char) + c) % len(lower_a)
        txt += lower_a[new]
    else:
        txt += char
print(txt)'''


   
'''upper_alph = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
text = 'Блажен, кто верует, тепло ему на свете!'
txt = ''
c = int(10)

for char in text:
    if char in upper_alph:
        new = (upper_alph.index(char) + c) % len(upper_alph)
        txt += upper_alph[new]
    elif char in lower_alph:
        new = (lower_alph.index(char) + c) % len(lower_alph)
        txt += lower_alph[new]
    else:
        txt += char
print(txt)'''


import random

word_list = ['мероприятие', 'гелиос', 'индикт', 'прогон', 'пистон', 'образ', 'телеграф']

def get_word():
    word = random.choice(word_list)
    return word.upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    print(word)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input('Введите букву или слово целиком в верхнем регистре: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Вы уже называли букву', guess)
            elif guess not in word:
                print('Буквы', guess, 'нет в слове.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Буква', guess, 'имеется в слове!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for i in indices:
                    word_as_list[i] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    print('Победа')
                    break
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('Вы уже называли слово', guess)
            elif guess != word:
                print('Слово', guess, 'не является верным.')
                tries -= 1
                guessed_words.append(guess)
            else:
                word_completion = word
                print('Победа')
                break
        else:
            print('Введите букву или слово.')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('Вы не угадали слово. Загаданным словом было ' + word + '. Может быть в следующий раз!')


ag = 'д'

while ag.lower() == 'д':
    word = get_word()
    play(word)
    ag = input('Играем еще раз? (д = да, н = нет):')
    











