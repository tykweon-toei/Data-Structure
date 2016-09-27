def factorial(num):
    res=1
    for k in range(1, num+1):
        res=k*res
    return res

num= input("Input Number : ")

print("Result : "+str(factorial(int(num))))