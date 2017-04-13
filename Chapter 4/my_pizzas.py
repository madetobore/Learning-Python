my_pizzas = ["cheese", "pepperoni", "bacon"]
friend_pizzas = my_pizzas[:]

my_pizzas.append('pineapple')
friend_pizzas.append('sausage')
# for pizza in pizzas:
#   # print (pizza)
#   print("I like " + pizza + " pizza")
# print("I really love pizza!")
print("My favorite pizzas are:")
for pizza in my_pizzas:
  print(pizza)

print("My friend's favorite pizzas are")
for pizza in friend_pizzas:
  print(pizza)
  