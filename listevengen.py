def squares(limit):
  for n in range(1,limit+1): 
   if n%2==0:
    yield i**2

# ex call
for s in squares(10):
    print(s)
