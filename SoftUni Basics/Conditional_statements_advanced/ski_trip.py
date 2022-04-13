days_staying = int(input())
type_room = input()
score = input()

nights_staying = days_staying - 1
room = 18 * nights_staying
apartment = 25 * nights_staying
president_apartment = 35 * nights_staying
discount = 0
score_diff = 0
total_price = 0


if days_staying < 10:
    if type_room == 'room for one person':
        total_price = room
        if score == 'positive':
            score_diff = total_price * 0.25
            total_price += score_diff
        elif score == 'negative':
            score_diff = total_price * 0.1
            total_price -= score_diff
    elif type_room == 'apartment':
        discount = apartment * 0.3
        total_price = apartment - discount
        if score == 'positive':
            score_diff = total_price * 0.25
            total_price += score_diff
        elif score == 'negative':
            score_diff = total_price * 0.1
            total_price -= score_diff
    elif type_room == 'president apartment':
        discount = president_apartment * 0.1
        total_price = president_apartment - discount
        if score == 'positive':
            score_diff = total_price * 0.25
            total_price += score_diff
        elif score == 'negative':
            score_diff = total_price * 0.1
            total_price -= score_diff
elif 10 <= days_staying <= 15:
    if type_room == 'room for one person':
        total_price = room
        if score == 'positive':
            score_diff = total_price * 0.25
            total_price += score_diff
        elif score == 'negative':
            score_diff = total_price * 0.1
            total_price -= score_diff
    elif type_room == 'apartment':
        discount = apartment * 0.35
        total_price = apartment - discount
        if score == 'positive':
            score_diff = total_price * 0.25
            total_price += score_diff
        elif score == 'negative':
            score_diff = total_price * 0.1
            total_price -= score_diff
    elif type_room == 'president apartment':
        discount = president_apartment * 0.15
        total_price = president_apartment - discount
        if score == 'positive':
            score_diff = total_price * 0.25
            total_price += score_diff
        elif score == 'negative':
            score_diff = total_price * 0.1
            total_price -= score_diff
else:
    if type_room == 'room for one person':
        total_price = room
        if score == 'positive':
            score_diff = total_price * 0.25
            total_price += score_diff
        elif score == 'negative':
            score_diff = total_price * 0.1
            total_price -= score_diff
    elif type_room == 'apartment':
        discount = apartment * 0.5
        total_price = apartment - discount
        if score == 'positive':
            score_diff = total_price * 0.25
            total_price += score_diff
        elif score == 'negative':
            score_diff = total_price * 0.1
            total_price -= score_diff
    elif type_room == 'president apartment':
        discount = president_apartment * 0.20
        total_price = president_apartment - discount
        if score == 'positive':
            score_diff = total_price * 0.25
            total_price += score_diff
        elif score == 'negative':
            score_diff = total_price * 0.1
            total_price -= score_diff

print(f'{total_price: .2f}')