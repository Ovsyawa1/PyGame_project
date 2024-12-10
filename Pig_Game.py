import random

print("Правила игры просты! От игроков требуется набрать как можно больше очков, кидая кость.\n Если число очков становится больше или равно 50, игрок сразу побеждает!")
print("Если во время своего хода игрок решил не бросать кость, то к его очкам прибавляется число его ходов.\n Однако, если игроку выпадет 1, то прибавляется 0 очков!\n")

def roll_the_dice(): # функция по созданию рандомного числа от 1 до 6
    roll = random.randrange(1, 7)
    return roll

while True: # в этом блоке будет определение числа игроков
    try:
        players = int(input("Введите число игроков (от 2 до 4): "))
    except ValueError:
        print("Необходимо ввести именно число") # если возникла ошибка типа данных, то пусть пользователь введет значение по-новой
        continue

    if (players > 4) or (players < 2):
        print ("Введите корректное число игроков") # если пользователь вбил некорректное число игроков то по-новой

    else:
        print("Игра начинается\n") # если всё прошло гладко, переходим к другому блоку
        break

players_score = [0 for _ in range(0, players)] # число очков каждого игрока хранится в массиве
turns_numb = [1 for _ in range(0, players)] # номер хода каждого игрока
which_turn = random.randrange(1, players + 1) # переменная, для определения "чей ход?"

print (f"Первым ходит игрок под номером: {which_turn}")

while True:
    turn = which_turn - 1

    print(f"Ход номер {turns_numb[turn]}")
    print(f"Игрок под номером {which_turn}, желаете ли бросить кость?")

    player_answer = str(input("Введите 'y' или 'n': "))

    if player_answer == "y":
        roll = roll_the_dice()
        print(f"Вам выпало число {roll}")
        if roll == 1:
            print("Unlucky")
        else:
            players_score[turn] += roll

    elif player_answer == "n":
        players_score[turn] += turns_numb[turn]

    else:
        print("Введите корректный ответ")
        continue

    turns_numb[turn] += 1
    print (f"Счет игрока {which_turn} равен {players_score[turn]}\n")

    if players_score[turn] >= 50:
        print(f"Победил игрок под номером {which_turn}")
        break

    if which_turn >= players:
        which_turn = 1
    else:
        which_turn += 1