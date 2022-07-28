numbers=[300,500,200]
out=map(str,numbers)
out=map(lambda i:i/10,numbers)
print(list(out))
print(tuple(out))