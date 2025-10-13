prev = int(input())
curr = int(input())

if curr >= prev:
    volume = curr - prev
else:
    volume = 10000 - prev + curr

if volume <= 300:
    cost = 21.00
elif volume <= 600:
    cost = 21.00 + (volume - 300) * 0.06
elif volume <= 800:
    cost = 21.00 + 300 * 0.06 + (volume - 600) * 0.04
else:
    cost = 21.00 + 300 * 0.06 + 200 * 0.04 + (volume - 800) * 0.025

average_price = cost / volume

print(f"Предыдущее Текущее Использовано К оплате Ср. цена m^3")
print(f"   {prev}      {curr}       {volume}       {cost:.2f}       {average_price:.2f}   ")