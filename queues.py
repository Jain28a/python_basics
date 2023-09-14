from collections import deque

q = deque()

q.append('1st element')
q.append('2nd element')
q.append('3rd element')

print(q, '\n')

a = q.popleft()
print('The poppped element is :' , a)
b = q.popleft()
print('The poppped element is :' , b)
c = q.popleft()
print('The poppped element is :' , c)

