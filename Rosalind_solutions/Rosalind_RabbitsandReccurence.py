def rabbandrecc(x,y):
    a,b = 0,1
    for i in range(1,x):
        a,b = b,y*a+b
        print (a)
rabbandrecc(9,3)
