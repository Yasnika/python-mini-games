# 19-20.10.26 Виселица :)
k = [[
   '  _____',
   '  |    |',
   '  |',
   '  |',
   '  |',
   '__|__'
   ], 
   [
   '  _____',
   '  |    |',
   '  |    0',
   '  |',
   '  |',
   '__|__'
   ], 
   [
   '  _____',
   '  |    |',
   '  |    0',
   '  |    |',
   '  |',
   '__|__'
   ], 
   [
    '  _____',
    '  |    |',
    '  |    0',
    '  |   /|',
    '  |',
    '__|__'
    ], 
    [
    '  _____',
    '  |    |',
    '  |    0',
    '  |   /|\\',
    '  |',
    '__|__'
    ], 
    [
    '  _____',
    '  |    |',
    '  |    0',
    '  |   /|\\',
    '  |   /',
    '__|__'
    ], 
    [
    '  _____',
    '  |    |',
    '  |    0',
    '  |   /|\\',
    '  |   / \\',
    '__|__'
    ]]

import random
sp = [
    'крот', 'медведь', 'стрелец', 'шахта', 
    'метель', 'шутка', 'козырь', 'виселица', 
    'человечек', 'шторм', 'мед', 'сталица', 
    'скворечник', 'кошка'
    ]

def viselisa():
    flag = True
    print('Приветствую! Вы попали в игру "Виселица!"')
    print('Количество допустимых ошибок: 6') 

    for i in k[0]:
        print(i)

    slovo = random.choice(sp)

    blur = [i for i in ('_' * len(slovo))]
    print()
    print('Скрытое слово: ')
    print(*blur)

    cnt = 0  
    while flag:
        print()
        bukva = input('Введите букву: ')
        if bukva in slovo and len(bukva) == 1:
            flag1 = False
            for i in range(len(slovo)):            
                if slovo[i] == bukva and blur[i] == '_':
                    flag1 = True
                    blur[i] = bukva
                    break
            if flag1:
                print(*blur)
            else:
                print('Вы уже угадали эту букву!')
                
        elif len(bukva) > 1:
            print('Можно вводить за раз только 1 букву!')
 
        elif bukva not in slovo:
            cnt += 1
            print('Буквы нет в слове, попробуйте еще раз!')
            print(f'Осталось всего {6 - cnt} жизней')               
               
            for i in k[cnt]:
                print(i)

        if cnt == 6: 
            flag = False      
            print('Вы проиграли!')
        elif slovo == ''.join(blur):
            flag = False
            print('Поздравляю! Вы выйграли!')
        
while True:
    viselisa()    
    answer = input('Если хотите начать сначала, напишите "Да": ').lower()       
    if answer != 'да':
        break
        
