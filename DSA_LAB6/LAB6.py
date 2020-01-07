import numpy as np

# INSERTION SORT
# Number = np.array([12, 11, 13, 5, 6])
#
# for i in range(1, len(Number)):
#
#     Key = Number[i]
#     j = i - 1
#
#     while j >= 0 and Key < Number[j]:
#         Number[j + 1] = Number[j]
#         j -= 1
#     Number[j + 1] = Key
#
# for i in range(len(Number)):
#     print(Number[i], end=" ")





#Counting sort

# Arr = np.array([5, 3, 2, 5, 3, 1, 7])
# count = np.array([0 for i in range(10)])
# for i in range(len(Arr)):
#     count[Arr [i]] += 1
# print(count)
# for i in range(1, len(count)):
#     count[i] += count[i - 1]
# print(count)
# SortArr = np.array([0 for i in range (len(Arr))])
#
# # for i in range(len(Arr)):
# #     SortArr[count[Arr[i]] - 1] = Arr[i]
# #     count[Arr[i]] -= 1
#
# for i in range(len(Arr)):
#     count[Arr[i]] -= 1
#     SortArr[count[Arr[i]]] = Arr[i]
# print(SortArr)

# LINEAR Search

# Arr = np.array([55, 3, 2, 5, 33, 1, 7])
# print(Arr)
# num = str(input("enter a  index: "))
# Flag = False
# num = int(input("enter a number index: "))
# for i in range(len(Arr)):
#     if num == Arr[i]:
#         Flag = True
#         break
# if Flag:
#     print("Number found index: " + str(i))
#
# else:
#     print("not found")


# string

# Arr = np.array(["Umer","Ali","Saqib","Faraz"])
# print(Arr)
# num = str(input("enter a  index: "))
# Flag = False
# for i in range(len(Arr)):
#     if num == Arr[i]:
#         Flag = True
#         break
# if Flag:
#     print("Number found index: " + str(i))
#
# else:
#     print("not found")


# BINARY SEARCH

Arr = np.array([21,22,23,24,25,26,28,29,30,31,33])
print(Arr)

Falg = False
first = 0
last = len(Arr) - 1

Value = int(input("enter a number: "))

while(first <= last):

    mid = int((first + last)/2)

    if  Value == Arr[mid]:
        Falg = True
        break


    elif Value < Arr[mid]:
        last = mid -1

    elif Value > mid:
        first = mid +1


if Falg:
    print("Number found index: " + str(mid))

else:
    print("not found")
