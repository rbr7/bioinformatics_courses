def fibonacci(n):
    n1=1
    n2=1
    i=0
    for i in range(n-1):
        nth=n1+n2
        n1=n2
        n2=nth
    return n1
print(fibonacci(25))
