#Formatting with .formate() method

print('this is a string {}' .format('INSERTED'))

print('The {} {} {}' .format('fox', 'brown', 'quick'))

print('The {2} {1} {0}' .format('fox', 'brown', 'quick'))

print('The {0} {0} {0}' .format('fox', 'brown', 'quick'))

print('The {c} {c} {c}' .format(b='fox', c='brown', d='quick'))


#Flow formatting  follows "{value:width.precision f}"

print(100/777)

print("the result is {r:1.2f}" .format(r=100/777))
print("the result is {r:1.4f}" .format(r=100/777))

print("the result is {:.2f}".format(100/777))

#Formatting of strings

name ="Prince"
print("Hello, his name is {}" .format(name))

print(f"Hello, his name is {name}")


