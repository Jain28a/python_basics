stack = []

def empty():
  if len(stack) == 0:
    print('Stack is empty.\n ')
  else:
    print(stack, '\n')

val1 = 11
val2 = 22
val3 = 33

stack.append(val1)
stack.append(val2)
stack.append(val3)
empty()

a = stack.pop()
b = stack.pop()
c = stack.pop()
print('The popped elements are : ', a, b, c, '\n')
empty()


