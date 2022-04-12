product = input()
city = input()
quantity = float(input())
price = 0

cities_dict = {"Sofia": {"coffee": 0.5,
                         "water": 0.8,
                         "beer": 1.2,
                         "sweets": 1.45,
                         "peanuts": 1.6},

               "Plovdiv": {"coffee": 0.4,
                           "water": 0.7,
                           "beer": 1.15,
                           "sweets": 1.30,
                           "peanuts": 1.5},

               "Varna": {"coffee": 0.45,
                         "water": 0.7,
                         "beer": 1.1,
                         "sweets": 1.35,
                         "peanuts": 1.55}
               }

if city in cities_dict:
    if product in cities_dict[city]:
        print(cities_dict[city][product] * quantity)


