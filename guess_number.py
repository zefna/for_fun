# -*- coding: utf-8 -*-
"""guess_number.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LzWl8cWSOnE3hqvWAFfKzrUNj7DxyiHj
"""

from random import *
num = randint(1, 100)
while True:
  print('Введите число:')
  user_num = int(input())
  if user_num == num:
      print('Вы угадали, поздравляем!')
      break
  elif user_num > num:
      print('Слишком много, попробуйте еще раз')
      continue
  else:
      print('Слишком мало, попробуйте еще раз')
      continue

from random import randint

print('Добро пожаловать в числовую угадайку')
print('Введите правую границу диапазона')

x = int(input())
num = randint(1, x)

def is_valid(n):
  if 0 < n < x + 1:
    return True
  else:
    return False

def new_game():
  counter = 0
  print(f'Введите число от 1 до {x}')
  while True:
    n = int(input())
    if is_valid(n) is False:
      print(f'А может быть все-таки введем целое число от 1 до {x}?')
      counter += 1
      continue
    elif n == num:
      counter += 1
      print(f'Поздравляем! Вы угадали с {counter} попытки :)')
      break
    elif n > num:
      print('Ваше число больше загаданного, попробуйте еще разок')
      counter += 1
      continue
    else:
      print('Ваше число меньше загаданного, попробуйте еще разок')
      counter += 1
      continue

new_game()

while True:
  print('Не желаете сыграть ещё раз? Да/нет')
  answer = input()
  if answer.lower() == 'да':
    print('Введите правую границу диапазона')
    x = int(input())
    num = randint(1, x)
    new_game()
  elif answer.lower() == 'нет':
    print('Спасибо, что играли в числовую угадайку. Аривидерчи')
    break
  else:
    print('Я не понял Ваш ответ, попробуйте снова')
    continue