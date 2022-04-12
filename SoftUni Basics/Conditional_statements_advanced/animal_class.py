type = ''
reptiles = ["crocodile", "tortoise", "snake"]
animal = input()

if animal == "dog":
    type = "mammal"
elif animal in reptiles:
    type = "reptile"
else:
    type = "unknown"

print(type)