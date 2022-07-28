f=lambda x:x+5*3
g=lambda x,y:x+5+y
print(f(2))
print(g(2,3))
print(f(4))
#lambda uses with mapping,filter,pandas
#these are function that will execute another function over every single element
numbers=[300,500,200]
out=map(str,numbers)
out=map(lambda i:i/10,numbers)