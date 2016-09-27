def factorial(num):

    if(num<=1):
        return 1
    else:
        return num*factorial(num-1)

num= input("Input Number : ")

print("Result : "+str(factorial(int(num))))