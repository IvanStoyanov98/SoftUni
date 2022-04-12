working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

day = input()

if day in working_days:
    print("Working day")
elif day in weekend:
    print(f"Weekend")
else:
    print("Error")