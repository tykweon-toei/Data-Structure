def slow_power(x, n):
    r=1
    for i in range(1, n+1):
        r=r*x
    return r

x= input("Input Number x : ")
n= input("Input Number n : ")

print("Result : "+str(slow_power(int(x), int(n))))
