import numpy as np


#Bubble sort:

# Numbers = np.array([1,5,2,4,3,6])
# count1 = 0
# print(Numbers)
#
# for i in range(len(Numbers) - 1):
#     count1 += 1
#     for j in range(len(Numbers) -1 -i):
#         count1 += 1
#         if Numbers[j] > Numbers[j+1]:
#             temp = Numbers[j]
#             Numbers[j] = Numbers[j +1]
#             Numbers[j +1] =temp
#
#
# print(Numbers)
# print(count1)

# buuble short with flag

# Numbers = np.array([1,2,4,3,5,6])
#
# print(Numbers)
#
# count = 0
# count1 = 0
# for i in range(len(Numbers) - 1):
#     count +=1
#     flag = False
#     for j in range(len(Numbers) -1 -i):
#         count += 1
#         if Numbers[j] > Numbers[j+1]:
#             temp = Numbers[j]
#             Numbers[j] = Numbers[j +1]
#             Numbers[j +1] =temp
#             flag = True
#     if  (not flag):
#         break
#
# print(Numbers)
# print(count)

# Sorting Strng Array:
# Numbers = np.array(['pakistan','America','China'],dtype=object)
# count1 = 0
# print(Numbers)
#
# for i in range(len(Numbers) - 1):
#     count1 += 1
#     for j in range(len(Numbers) -1 -i):
#         count1 += 1
#         if Numbers[j] > Numbers[j+1]:
#             temp = Numbers[j]
#             Numbers[j] = Numbers[j +1]
#             Numbers[j +1] =temp
#
#
# print(Numbers)
# print(count1)



# selection sort

# Numbers = np.array([20,8,5,10,5])
# print(Numbers,end=" ")
# for i in range(len(Numbers)):
#     min_index = i
#     for j in range(i + 1, len(Numbers)):
#         if Numbers[min_index] > Numbers[j]:
#             min_index = j
#     temp = Numbers[i]
#     Numbers[i] = Numbers[min_index]
#     Numbers[min_index] = temp
#
# for i in range(len(Numbers)):
#     print(Numbers[i],end=" ")


# if use

# Numbers = np.array([20,8,5,10,5])
# print(Numbers,end=" ")
# for i in range(len(Numbers)):
#     min_index = i
#     for j in range(i + 1, len(Numbers)):
#         if Numbers[min_index] > Numbers[j]:
#             min_index = j
#     if (Numbers[min_index] != Numbers[i]):
#         temp = Numbers[i]
#         Numbers[i] = Numbers[min_index]
#         Numbers[min_index] = temp
#
# for i in range(len(Numbers)):
#     print(Numbers[i],end=" ")


# INSERTION SORT:

# Number = np.array([12,11,13,5,6])
#
# for i in range(1, len(Number)):
#
#     Key = Number[i]
#     j = i - 1
#
#     while j >=0 and Key < Number[j]:
#
#         Number[j + 1] = Number[j]
#         j -=1
#     Number[j +1] = Key
#
# for i in range(len(Number)):
#     print(Number[i],end=" ")

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
# for i in range(len(Arr)):
#     SortArr[count[Arr[i]] - 1] = Arr[i]
#     count[Arr[i]] -= 1
# print(SortArr)



