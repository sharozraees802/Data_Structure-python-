import numpy as Array

number = int(input("ENTER THE VALUE : "))
fib = Array.array([0 for i in range(number)])
fib[0]=0
fib[1]=1

aa = 0
bb = 1

Array1 = []
Array2 = []

Array1.append(number)
Array1.append(aa)
Array1.append(bb)

#series

fseries = "fibonacci series:"
print(fseries, end=" ")
print(aa,end=" " + "" + str(bb)+" ")

for i in range(2,len(fib)):
    fib[i] = fib[i - 1] + fib[i - 2]
    if number == fib[i]:
        print(str(fib[i]), end=" ")

        break

    else:

        print(fib[i], end=" ")



# insert
for i in range(number - 1):
    sum = aa + bb
    aa = bb
    bb = sum
    if sum <= number:
        Array1.append(sum)

insert = "insert value:"
print(insert, end="")
print(Array1,end=" ")

# PRIME
for j in range(len(Array1)):
    flag = False
    for k in range(2, Array1[j]):
        if Array1[j] % k == 0:
            flag = True
            break
        else:
            continue

    if flag == False:
        if Array1[j] == 0 or Array1[j] == 1:
            pass
        else:
            Array2.append(Array1[j])

for p in range(len(Array2)):
    hold = Array2[p]

    for q in range(len(Array1)):
        if hold == Array1[q]:

            for z in range(q, len(Array1) - 1, 1):
                Array1[z] = Array1[z + 1]

# DELETE
primnum = "prime number:"
print(primnum, end=" ")
print(Array2,end=" ")
primnum = "Delete prime Number:"
print(primnum, end=" ")
print(Array1[:(len(Array1) - len(Array2))])