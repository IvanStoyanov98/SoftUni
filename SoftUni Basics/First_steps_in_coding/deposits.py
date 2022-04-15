deposited_sum = float(input())
due_period = int(input())
yearly_interest_rate = float(input())

interest = deposited_sum * (yearly_interest_rate / 100)
monthly_interest = interest / 12

print(f"{deposited_sum + due_period * monthly_interest}")