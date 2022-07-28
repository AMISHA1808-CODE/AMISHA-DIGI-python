def add(a,b,c=1,d=3):
   return a+b+c+d

if __name__=="__main__":
    print(add(a=1,b=2,c=3,d=4))
    print(add(20,3,5,7))
    print(add(20,20))
    print(add(c=40,d=30,a=20,b=30))
    print(add(d=30,a=20,b=30))