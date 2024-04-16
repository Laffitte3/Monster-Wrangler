import random

list = ["blue","purple","green","yellow"]

random_number= random.randint(0,3)
random_list = list[random_number]

print("Mi indice es: "+ str(random_number))
print(random_list)