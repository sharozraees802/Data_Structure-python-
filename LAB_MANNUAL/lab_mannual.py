import numpy as np
from timeit import Timer

# EX: 1.5

# FirstArray = np.array([0 for i in range(5)])
# length = len(FirstArray)
#
# for i in range(length):
#     FirstArray[i] = i + 1
# for i in FirstArray:
#     print(i)


# EX:1.6

# n = int(input("How many players name you want to Enter:"))
# playername = np.array([' ' for i in range(n)], dtype = object)
#
# for i in range(len(playername)):
#     print()
#     playername[i] = input(f"Enter player {(i + 1)} Name: ")
# print("Players Name");
# print("---------------------");
#
# for i in playername:
#     for j in range(len(playername)):
#         print((j+1), i)


# EX:1.7(insert value)


# def insertelement(LA,N,K,Item):
#     j = N - 1
#     while(j >= K ):
#         LA[j +1] = LA[j]
#         j = j -1
#     LA[K] = Item
#     N = N +1
#     return N
#
# def printArray(LA,N):
#     for i in range(N):
#         print(LA[i],end=" ")
# LA = np.array([0 for i in range(50)])
# N = int(input("Enter Array Length: "))
# for i in  range(N):
#     LA[i] =int(input(f"Enter Value Of Index {i}: "))
# printArray(LA,N)
#
# print()
# K = int(input("Enter Position where you want to add Element: "))
# Item = int(input(f"Enter Value Of {K} Position: "))
# N = insertelement(LA,N,K,Item)
# printArray(LA,N)


# EX:1.9 (insertvalue)


# Numbers = np.array([11,12,33,44,55])
#
# for i in range(len(Numbers)):
#     print(Numbers[i],end=" ")
# print()
# Index = int(input("Enter Index where you want to add value: "))
# Value = int(input(f"Enter value of Index {Index}: "))
#
# temp = np.array([0 for i in range((len(Numbers)+1))])
#
# j = 0
#
# for i in range(len(temp)):
#     if (i == Index):
#         temp[i] = Value
#     else:
#         temp[i] = Numbers[j]
#         j +=1
#
# Numbers = temp
#
# for i in range(len(Numbers)):
#     print(Numbers[i],end=" ")
# print()
# print("Array Length is: ",len(Numbers))


# EX 1.9(delete value)

# def delte(LA,N,K):
#     j = K +1
#     while (j < N):
#         LA[j - 1] = LA[j]
#         j +=1
#     N = N -1
#     return N
#
# LA = np.array([0 for x in range(20)])
# N = int(input("Enter Array Length:"))
#
# for i in range(N):
#     LA[i]=int(input(f"Enter a Value {(i +1)} of Index {i}: "))
#
# print("----------------------")
#
# for i in range(N):
#     print(LA[i],end=" ")
# print()
# K = int(input("Enter element index which you want to remove: "))
# N = delte(LA,N,K)
#
# for i in range(N):
#     print(LA[i],end=" ")

# EX: 1.10(delete value)

# Numbers = np.array([11,12,13,14,15])
#
# for i in range(len(Numbers)):
#     print(Numbers[i],end=" ")
#
# print()
# Index = int(input("Enter element index which you want to delete: "))
# Temp = np.array([0 for i in range(len(Numbers)-1)])
#
# j = 0
# for i in range(len(Numbers)):
#     if i == Index:
#         continue
#     else:
#         Temp[j] = Numbers[i]
#         j += 1
# Numbers = Temp
#
# for i in range(len(Numbers)):
#     print(Numbers[i],end=" ")


# EX:1.11

size_of_vec = 1000
x_list = range(size_of_vec)
y_list = range(size_of_vec)
x = np.array(size_of_vec)
y = np.array(size_of_vec)



def pure_python_version():
    z = [x_list[i] + y_list[i] for i in range(len(x_list))]
    
    
def numpy_version():
    z = x + y

time_obj1 = Timer("pure_python_version()","from __main__ import pure_python_version")

time_obj2 = Timer("numpy_version()","from __main__ import numpy_version")
 
print(time_obj1.timeit(200))
print(time_obj2.timeit(200))

# print(time_obj1.repeat(repeat=3,number=200))
# print(time_obj2.repeat(repeat=3,number=200))