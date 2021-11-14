from random import *
seeds = 0
seed(seeds)
num2 = randint(1,100)
print(num2)
print('Добро пожаловать в числовую угадайку! Введите целое число от 1 до 100: ')

def is_valid(number):
    return number in list(range(1, 101))

count = 0
num = 0
while num2 != num:
    num = int(input())
    if is_valid(num) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    count += 1
    if num < num2:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    if num > num2:
        print('Ваше число больше загаданного, попробуйте еще разок')
    if num2 == num: 
        print("Вы угадали, поздравляем!", "Количество попыток =", count)
        print('Попробуем ещё раз? введите (д - ДА или н - НЕТ)')
        restart_answer = input()
        if restart_answer == 'д':
            seeds += 1
            continue
        else:
            if restart_answer == 'н' or restart_answer != 'д':
                break
    num = 0
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')