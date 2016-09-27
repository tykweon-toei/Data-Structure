def fib(n):
    if n<=2:
        return n
    else:
        cnt=1
        last=0
        for i in range(2, n+1):
            tmp = cnt
            cnt = cnt + last
            last = tmp
        return cnt

num= input("Input Number : ")

print("Result : "+str(fib(int(num))))