packets = input()
lost_pack = 0
max_lost_streak = 0
current_streak = 0
if len(packets) < 5:
    print('Длина последовательности должна быть не меньше 5')
    exit(0)
if not all(char in '01' for char in packets):
    print('Неверный ввод. Используйте только символы "0" и "1"')
    exit(0)
for packet in packets:
        if packet == '0':
            lost_pack += 1
            current_streak += 1
            max_lost_streak = max(max_lost_streak, current_streak)
        else:current_streak = 0
loss_percentage = (lost_pack / len(packets)) * 100
if loss_percentage <=1:
    quality = 'Отличное качество'
elif loss_percentage <= 5:
    quality = 'Хорошее качество'
elif loss_percentage <= 10:
    quality = 'Удовлетворительное качество'
elif loss_percentage <= 20:
    quality = 'Плохое качество'
else:
    quality = 'Критическое состояние сети'
print('Общее количество пакетов:', len(packets))
print('Количество потерянных пакетов:', packets.count('0'))
print('Длина самой длинной последовательности потерянных пакетов:', max_lost_streak)
print(f'Процент потерь: {lost_pack / len(packets) * 100}%')
print('Качество связи:', quality)