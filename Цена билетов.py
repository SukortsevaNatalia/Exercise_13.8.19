cost = 0
number_people = int(input('Укажите количество людей, планирующих посетить конференцию: '))

for i in range(number_people):
    age = int(input(f'Укажите возраст посетителя № {i+1}: '))

    if age < 18:
        continue
    elif 18 <= age < 25:
        cost += 990
    else:
        cost += 1390

if number_people > 3:
    cost = cost - cost * 0.1
    print(f'Сумма к оплате (с учетом скидки 10%): {cost} руб.')
else:
     print(f'Сумма к оплате: {cost} руб.')
