def SquareOfNumbers(n):
    if (n < 0 or n > 100):
        return
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    print(d)
    return

n = eval(input("Enter a Number (1-100): "))
SquareOfNumbers(n)