# import sys
#
# sys.setrecursionlimit(2000)
#
# print(sys.getrecursionlimit())
#
# i = 0
#
# def greet():
#     global i
#     i+=1
#     print("Hello",i)
#     greet()                             #Recursion is Function calling itself.
#
# greet()


import sys

sys.setrecursionlimit(1000000000)

print(sys.getrecursionlimit())
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)


n = int(input('Enter the number for which you need to calculate factorial:-')) ##6449

result = fact(n)
print(result)

