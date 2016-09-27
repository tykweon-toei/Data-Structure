def power(x, n):
    r=1
    if n==0:
        return 1
    elif (n%2)==0:
        return power(x*x, n/2)
    else:
        return x*power(x*x, (n-1)/2)

x= input("Input Number x : ")
n= input("Input Number n : ")

print("Result : "+str(power(int(x), int(n))))
