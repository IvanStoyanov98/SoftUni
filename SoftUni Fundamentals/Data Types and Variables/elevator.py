number_of_ppl = int(input())
capacity = int(input())
extra_course = 0
number_of_courses = number_of_ppl // capacity

if number_of_ppl % capacity != 0:
    left = number_of_ppl % capacity
    extra_course += 1

print(number_of_courses + extra_course)