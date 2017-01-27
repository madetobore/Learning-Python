list = ['jc', 'mj', 'j']
message = "Would you like to go to dinner, "
print(message + list[0] + "?")
print(message + list[1] + "?")
print(message + list[2] + "?")

print(list[1] + " can't make it")
del list[1]
list.insert(1, 'me')
print(message + list[1] + "?")

print("There's more room now")

list.insert(0, 'you')
list.insert(2, 'not you')
list.append('them')

print(list)

print("Only two people")
list_popped = list.pop()
print("Sorry you can't come, " + list_popped)
list_popped = list.pop()
print("Sorry you can't come, " + list_popped)
list_popped = list.pop()
print("Sorry you can't come, " + list_popped)
list_popped = list.pop()
print("Sorry you can't come, " + list_popped)

message = "You can come, "
print(message + list[0])
print(message + list[1])

del list[0]
del list[0]

print(list)