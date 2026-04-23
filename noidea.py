import sys

line1=input()
line2=input()
line3=input()
line4=input()
arr=[]
a=[]
b=[]
n,m=line1.split(" ")
arr=line2.split(" ")
a=line3.split(" ")
b=line4.split(" ")
happiness=0
n,m=int(n),int(m)
arr= list(map(int,arr))
a= set(list(map(int,a)))
b= set(list(map(int,b)))  #turns each element to int seperatly
if m in range(1,pow(10,5)+1) and n in range(1,pow(10,5)+1):
    for i in arr:
        if i in range(1,pow(10,9)+1):
            if i in a:
                happiness+=1
            elif i in b:
                happiness-=1
        else:
            sys.exit()
    print(happiness)
else:
    sys.exit()