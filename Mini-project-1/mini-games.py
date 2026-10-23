
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
                            # МЕНЮ
def menu():
    print('    МЕНЮ')
    print('Выберите игру:') 
    print('1. Быки и коровы')
    print('2. Виселица')
    print('3. Камень-ножница-бумага')

    vibor = int(input('Введите номер игры: '))
                            # БЫКИ И КОРОВЫ
    import random                       
    if vibor == 1:
        print()
        print('Приветствую! Вы попали в игру "Быки и коровы"')
        print()
        print('Правила просты: вам необходимо угадать случайное 4-значное число загаданное игрой.')
        print('Подсчет быков говорит о количестве правильных цифр на правильных позициях,') 
        print('а количество коров о цифрах которые есть но стоят не на своих местах')
        print()
        print('ВАЖНОЕ УТОЧНЕЕ: цифры не повторяются!')

        sp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        def bik_kor():
            rand_ch = str(random.sample(sp, 4))   
            cnt = 0
            flag = True

            while flag:
                print()

                user_1 = int(input('Введите 4-значное число: '))
                user = [i for i in str(user_1)]
                bulls = 0
                cows = 0

                if len(user) == 4 and len(set(user)) == 4:
                    for i in user:
                        if i in rand_ch:
                            if user.index(i) == rand_ch.index(i):
                                bulls += 1
                            elif user.index(i) != rand_ch.index(i):
                                cows += 1

                elif len(user) > 4:
                    print('Вы ввели слишком много цифр, нужно ровно 4')
                elif len(user) < 4:
                    print('Вы ввели слишком мало цифр, нужно ровно 4')
                elif len(set(user)) < 4:
                    print('Цифры должны отличаться друг от друга')
        
                cnt += 1
                print(f'Быки = {bulls}')
                print(f'Коровы = {cows}')
                print(f'Попыток осталось {10 - cnt}')

                if cnt == 10:
                    flag = False
                    print('Вы проиграли')
                elif bulls == rand_ch:
                    flag = False
                    print('Поздравляю, вы смогли отгадать все цифры!')
        bik_kor()
    
                                   # ВИСЕЛИЦА
    elif vibor == 2:           
        sp = [
    'крот', 'медведь', 'стрелец', 'шахта', 
    'метель', 'шутка', 'козырь', 'виселица', 
    'человечек', 'шторм', 'мед', 'сталица', 
    'скворечник', 'кошка'
    ]

        def viselisa():
            flag = True
            print('Приветствую! Вы попали в игру "Виселица!"')
            print('Количество попыток: 6') 

            for i in k[0]:
                print(i)

            slovo = random.choice(sp)

            blur = [i for i in ('_' * len(slovo))]
            print()
            print('Скрытое слово: ')
            print(*blur)

            cnt = 0     
            buk = []        
            while flag:
                print()
                bukva = input('Введите букву: ').strip()                                             
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
                    if bukva not in buk:
                        buk.append(bukva)
                        cnt += 1
                        print('Буквы нет в слове, попробуйте еще раз!')
                        print(f'Осталось всего {6 - cnt} жизней')

                        for i in k[cnt]:
                            print(i)

                    else:
                        print('Вы уже использовали данную букву!')               
                               
                   
                if cnt == 6: 
                    flag = False      
                    print('Вы проиграли!')
                elif slovo == ''.join(blur):
                    flag = False
                    print('Поздравляю! Вы выйграли!')
        
        viselisa()

                                      # КАМЕНЬ-НОЖНИЦА-БУМАГА

    elif vibor == 3:
        import random
        def k_n_b():
            print('Приветствую! Это игра в камень-ножница-бумага')
            print('Во время игры вводить нужно лишь первые буквы: камень = к, ножница = н, бумага = б')
            print('Для победы необходимо набрать 3 очка')
            print()
            print('Вашего соперника зовут Стив')

            sp = ['к', 'н', 'б']
    
            cnt_stiv = 0
            cnt_user = 0
            print()
            name = input('Введите свое имя: ')
            print()

            while cnt_user < 3 and cnt_stiv < 3:
                stiv = random.choice(sp)
                print()
                user = input('Ваш ход: ')
                print(f'Ход противника: {stiv}')
                print()

                if stiv == user:
                    print('ничья')

                elif stiv == 'к' and user == 'н':
                    print('победил Стив')
                    cnt_stiv += 1
                elif stiv == 'к' and user == 'б':
                    print(f'победил {name}!')
                    cnt_user += 1
                elif stiv == 'н' and user == 'к':
                    print(f'Победил {name}!')
                    cnt_user += 1
                elif stiv == 'н' and user == 'б':
                    print('Победил Стив')
                    cnt_stiv += 1
                elif stiv == 'б' and user == 'к':
                    print('Победил Стив')
                    cnt_stiv += 1
                elif stiv == 'б' and user == 'н':
                    print(f'Победил {name}!')

                print(f'Стив = {cnt_stiv}')
                print(f'{name} = {cnt_user}')

                if user not in sp:
                    print('Пожалуйста введите одну из выше указанных букв!')
                elif not user.isalpha():
                    print('Вы ввели не букву! (надо к, н или б)')
                elif len(user) > 1:
                    print('Cлишком много символов')

                if cnt_user == 3:
                    print('Поздравляю, вы победили!')
                else:
                    print('Вы проиграли')
        k_n_b()

    else:
        print('Пожалуйста введите одну из перечисленных цифр для выбора игры')
    

# Возврат к меню      
while True:
    menu()
    us = int(input('Чтобы вернуться к меню введите "1": '))
    print()
    if us != 1:
        break
