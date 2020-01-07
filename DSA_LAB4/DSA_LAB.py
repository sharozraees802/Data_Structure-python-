import numpy as Array
from timeit import Timer
# 1.08
# Numbers = Array.array([11,22,33,44,55])
# for i in range(len(Numbers)):
#     print(Numbers[i], end=" " )
# Index = int(input("Enter Index where you want to add Value: "))
# value = int(input(f"Enter Value of Index {Index}:"))
# temp = Array.array([0 for i in range(len(Numbers)+1)])
# j = 0
# for i in range(len(temp)):
#     if i == Index:
#         temp[i] = value
#     else:
#         temp[i] = Numbers[j]
#         j +=1
# Numbers = temp
# for i in range(len(Numbers)):
#     print(Numbers[i], end=" ")
# print("Array  Length is :", len(Numbers))


# 1.09
# def delete(LA,N,k):
#     j = k + 1
#     while j < N:
#         LA[j-1] = LA[j]
#         j +=1
#     N = N -1
#     return N
# LA = Array.array([0 for i in range(20)])
# N = int(input("Enter A Array Length "))
# for i in range(N):
#     LA[i] = int(input(f"Enter Value of index: {(i + 1)}: "))
# print("-------------")
# for i in range(N):
#     print(LA[i], end=" ")
#
# k = int(input("Enter element index which you want to remove: "))
# N = delete(LA, N, k)
#
# for i in range(N):
#     print(LA[i], end=" ")

# 1.10

Numbers = Array.array([11,12,13,14,15])

for i in range(len(Numbers)):
    print(Numbers[i], end=" ")
Index = int(input("Enter element index which you want to delete "))
Temp = Array.array([0 for i in range(len(Numbers)-1)])
j =0
for i in range(len(Numbers)):
    if  i == Index:
        continue
    else:
         Temp[j] = Numbers[i]
         j +=1
         Numbers = Temp
for i in range(len(Numbers)):
    print(Numbers[i], end = " ")
# 1.11


