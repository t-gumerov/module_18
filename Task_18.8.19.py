cost = 0
number_of_tickets = int(input('Введите цифрами количество билетов: '))
for i in range(number_of_tickets):
    i += 1
    age_by_ticket = int(input(f'Введите цифрами количество полных лет посетителя по {i} билету: '))
    if age_by_ticket < 18:
            print('Цена билета - 0 руб.')
    elif 18 <= age_by_ticket < 25:
            cost += 990
            print('Цена билета - 990 руб.')
    else:
            cost += 1390
            print('Цена билета - 1390 руб.')
if number_of_tickets > 3:
    total_cost = cost - ((cost / 100) * 10)
    print(f'Сумма к оплате - {total_cost} руб. (учитывая дополнительную скидку 10%, т.к. Вы регистрируете больше трёх человек!)')
else:
    print(f'Сумма к оплате - {cost} руб.')