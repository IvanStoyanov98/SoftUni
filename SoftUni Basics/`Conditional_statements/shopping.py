budget = float(input())
video_cards = int(input()) * 250
processors = int(input()) * (video_cards * 0.35)
ram = int(input()) * (video_cards * 0.1)

total = video_cards + processors + ram

if video_cards / 250 > processors / (video_cards * 0.35):
    total *= 0.85

if total >= budget:
    print(f"You have {abs(budget - total):.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(budget - total):.2f} leva more!")