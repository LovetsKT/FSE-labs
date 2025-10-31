import random
import time

N = int(input('Введите количество примеров:'))
total_time = 0
counter_answer = 0
for i in range(N):
    print (f'Вопрос {i+1}/{N}')
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    start_time = time.time()
    while True:
        try:
            answer = int(input(f'{a} * {b} = '))
            break
        except ValueError:
            print('Пожалуйста, введите целое число')
    time_spend = time.time() - start_time
    total_time += time_spend
    if answer == a * b:
        print('Верно!')
        counter_answer += 1
    else:
        print('Неверно!')
    print(f'Время:', time_spend)
print('=============================================')
print('СТАТИСТИКА')
print('=============================================')
print('Общее время:', total_time)
print('Среднее время на вопрос:', total_time / N)
print(f'Правильных ответов: {counter_answer}/{N}')
print(f'Процент правильных ответов: {(counter_answer / N) * 100}%')