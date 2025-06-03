a=8796
s=0
s1=0
n=a
while n:
    r=n%10
    s+=r
    n//=10
if s<10:
    print(s)
else:
    p=s%10
    s1+=p
    p//=10
    print(s1)

    