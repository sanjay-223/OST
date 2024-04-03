n = 5
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)

for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()