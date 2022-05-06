def loading_bar(percentage):
    bar = ["."] * 10
    number = percentage // 10

    for a in range(number):
        bar[a] = "%"

    if percentage != 100:
        print(f'{percentage}% [{"".join(bar)}]')
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f'[{"".join(bar)}]')


users_input = int(input())
loading_bar(users_input)