a1=set()
a2=set()
a3=set()
a4=set()
a5=set()
a6=set()
b=0
while True:
    b+=1
    for i in (str(b)):
        a1.add(i)
    for i in (str(2*b)):
        a2.add(i)
    for i in (str(b*3)):
        a3.add(i)
    for i in (str(b*4)):
        a4.add(i)
    for i in (str(b*5)):
        a5.add(i)
    for i in (str(b*6)):
        a6.add(i)
    if a1==a2==a3==a4==a5==a6:
        print(b)
        break
    else:
        a1.clear()
        a2.clear()
        a3.clear()
        a4.clear()
        a5.clear()
        a6.clear()

    
