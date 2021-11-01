from math import sqrt
a = int(input()) #1234

a1 = a%10 # 4
a //= 10 # 123

a2 = a%10 # 3
a //= 10 # 12

a3 = a%10 # 2
a //=10 # 1

a4=a%10

print(a1%2*a1,a2%2*a2,a3%2*a3,a4%2*a4)

