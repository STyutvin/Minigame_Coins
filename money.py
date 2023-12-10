# тест на правильность ввода количества монет
def user_coins(n):
  while True:
    n = int(input('Сколько возьмешь монет? '))
    if 0 >= n or n > 3:
      print('Не жульничай! Можно брать только от 1 до 3 монет.\n')
    else:
      break
  return n


# если игрок выбрал ходить первым
def user_turn():
  coins = 11

  user_choice = None
  bot_choice = None

  print('Ход игрока:')
  user_choice = user_coins(user_choice)
  coins = coins - user_choice
  print(f'Осталось {coins}\n')

  if user_choice == 1:
    # ход бота
    bot_choice = 1
    print('Ход компьютера:')
    print(f'Я возьму {bot_choice}')
    coins = coins - bot_choice
    print(f'Осталось {coins}\n')
    while coins != 1:
      # ход юзера
      print('Ход игрока:')
      user_choice = user_coins(user_choice)
      coins = coins - user_choice
      print(f'Осталось {coins}\n')
      # ход бота
      bot_choice = 4 - user_choice
      print('Ход компьютера:')
      print(f'Я возьму {bot_choice}')
      coins = coins - bot_choice
      print(f'Осталось {coins}\n')
    print('Ты проиграл, мой юный друг.\n')
  elif user_choice == 3:
    # ход бота
    bot_choice = 3
    print('Ход компьютера:')
    print(f'Я возьму {bot_choice}')
    coins = coins - bot_choice
    print(f'Осталось {coins}\n')
    while coins != 1:
      # ход юзера
      print('Ход игрока:')
      user_choice = user_coins(user_choice)
      coins = coins - user_choice
      print(f'Осталось {coins}\n')
      # ход бота
      bot_choice = 4 - user_choice
      print('Ход компьютера:')
      print(f'Я возьму {bot_choice}')
      coins = coins - bot_choice
      print(f'Осталось {coins}\n')
    print('Ты проиграл, мой юный друг.\n')
  else:
    # ход бота
    bot_choice = 1
    print('Ход компьютера:')
    print(f'Я возьму {bot_choice}')
    coins = coins - bot_choice
    print(f'Осталось {coins}\n')
    # ход юзера
    print('Ход игрока:')
    user_choice = user_coins(user_choice)
    coins = coins - user_choice
    print(f'Осталось {coins}\n')
    if user_choice == 1 or user_choice == 2:
      # ход бота
      bot_choice = coins - 5
      print('Ход компьютера:')
      print(f'Я возьму {bot_choice}')
      coins = coins - bot_choice
      print(f'Осталось {coins}\n')
      while coins != 1:
        # ход юзера
        print('Ход игрока:')
        user_choice = user_coins(user_choice)
        coins = coins - user_choice
        print(f'Осталось {coins}\n')
        # ход бота
        bot_choice = 4 - user_choice
        print('Ход компьютера:')
        print(f'Я возьму {bot_choice}')
        coins = coins - bot_choice
        print(f'Осталось {coins}\n')
      print('Ты проиграл, мой юный друг.\n')
    else:
      # ход бота
      print('Ход компьютера:')
      print('Ладно, умник, так и быть, возьму 3 монеты. Остается 2. Твой ход, смотри - не перенапрягись.\n')
      bot_choice = 3
      coins = coins - bot_choice
      # ход юзера
      print('Ход игрока:')
      while user_choice != 1:
        user_choice = user_coins(user_choice)
        if user_choice != 1:
          print('\nДве монеты осталось, гений!\n')
        else:
          break
      coins = coins - user_choice
      print(f'Осталось {coins}\n')
      print('Ты победил!')


# если игрок выбрал ходить вторым
def bot_turn():
  coins = 11

  user_choice = None
  bot_choice = None

  # ход бота
  bot_choice = 2
  print('Ход компьютера:')
  print(f'Отлично! Тогда я возьму {bot_choice}')
  coins = coins - bot_choice
  print(f'Осталось {coins}\n')
  while coins != 1:
    # ход юзера
    print('Ход игрока:')
    user_choice = user_coins(user_choice)
    coins = coins - user_choice
    print(f'Осталось {coins}\n')
    # ход бота
    bot_choice = 4 - user_choice
    print('Ход компьютера:')
    print(f'Я возьму {bot_choice}')
    coins = coins - bot_choice
    print(f'Осталось {coins}\n')
  print('Ты проиграл, мой юный друг.\n')


# запуск игры

print('Игра "Монетки".\n')
print('На столе 11 монет. Каждый игрок по очереди берет от 1 до 3 монет.')
print('Проигрывает тот, кто забирает последнюю монету.\n')
flag = 0
while flag != 1:
  turn_choice = input('Желаешь ли начать первым (д/н)? ').lower()
  print()
  if turn_choice == 'д' or turn_choice == 'да':
    user_turn()
    again = input('Сыграем еще раз (д/н)? ').lower()
    if again == 'н' or again == 'нет':
      flag = 1
  elif turn_choice == 'н' or turn_choice == 'нет':
    bot_turn()
    again = input('Сыграем еще раз (д/н)? ').lower()
    if again == 'н' or again == 'нет':
      flag = 1
  else:
    print('Нужно ввести "д" или "да", либо "н" или "нет". Регистр не важен.\n')