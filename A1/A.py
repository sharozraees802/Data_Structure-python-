import numpy as Array
# import nparray as ar
user = int(input("Enter a number of Element: "))
fib = Array.array([0 for i in range(user+1)])
fib1 = Array.array([0 for i in range(user+1)])
fib2 = Array.array([0 for i in range(user+1)])
# s = ar.array([0 for i in range(user+1)])
# fib=Array.insert()
fib[0]=0
fib[1]=1
f = 0
s = 1

fseries = "fibonacci series:"
print(fseries, end=" ")
print(f , end="" + "  " + str(s)+" ")

for i in range(2,len(fib)):
    fib[i] = fib[i - 1] + fib[i - 2]
    if user == fib[i]:
        print(str(fib[i]), end=" ")

        break

    else:
        print(fib[i], end=" ")

insert = "insert value:"
print(insert, end="")
index = 0
value = user
temp = Array.array([0 for i in range(len(fib)+1)])
j = 0
for i in range(len(temp)):
    if i == index:
        temp[i]=value
    else:
        temp[i]=fib[j]
        j +=1
fib = temp
for i in range(len(fib)):

    print(fib[i], end=" ")



primnum = "prime number:"
print(primnum, end=" ")

for i in range(2,len(temp)):
    v = False
    if temp[i] != 1:
        d=2
        while(d<i):
            if temp[i]%d==0 :
                if temp[i]%d:
                    v = True
                    break
            d +=1
        else:
            # fib1 = temp
            v = True
            print(temp[i], end=" ")


# if len(fib)>1:
#     for i in range(2, len(fib)):
#         if fib[i] % i ==0:
#             break
#         else:
#             print(fib[i], end=" ")

# for num in range (2,len(fib)):
#if fib[i] != 1:
#     d=2
#     while(d<=fib[num]/2):
#         if fib[num]%d==0 :
#             if fib[num]%d:
#                 break
#         d +=1
#     else:
#         fib1 = fib
#         print(fib1[num], end=" ")

# for y in range(1,len(fib)):
#     x = int(y)
#     for x in range(2,x):
#         if (y/x).is_integer():
#             len(fib).append(x)
#     if len(fib) < 2:
#         fib1.append(y)
#
# print(fib1)

# def prime(num):
#     s =0
#     flag = 0
#     for i in range(s, num/2):
#         if num%i ==0:
#             flag = 1
#             break
#         s+=1
#     if flag==1:
#         return 0
#     else:
#         return 1
#
#
#
#
# loop=0
# length = int(len(fib)/len(fib[0]))
# for i in  range(loop,length):
#     print(fib[loop])
# loop+=1
# lower = 0
# uper = 0
# c = 0
# counter = 3
# for num in range(c,user):
#     lower = int(fib[num] / 2)
#     for i in range(2,lower):
#         if fib[num]%i  ==0:
#             fib1[num]=fib[num]
#             uper = 1
#             break
#
#
#     if uper ==0:
#         if fib[num] >=2:
#             fib2[num] = fib[num]
#         else:
#             fib1[num] = fib[num]
#
#
# for i in range(2,len(fib1)):
#     if fib1[i] == 0:
#         continue
#     print(fib1[i], end=" ")
# for num in  range(lower, len(fib)+1):
#     if num > 1:
#         for i in range(2,num):
#             if num%i == 0:
#                 break
#             else:
#                 print(num, end=" ")
#
#
#
