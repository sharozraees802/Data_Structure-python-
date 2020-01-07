import numpy as Array
n1=0
n2=0
n3=0
i =0
number = int(input("Enter the number of elements: "))
arr1 = Array.array([0 for i in range(number+5)])
arr2 = Array.array([0 for i in range(number+5)])
FinalState = Array.array([0 for i in range(number+5)])
for q in  range(2,(number+5)):
    arr1[q]=0
    arr2[q]=0
    FinalState[q]=0
print("\nFab Series : ")
print(str(n1) + " " + str(n2) + " ")
arr1[0]=number
arr1[1]=n1
arr1[2]=n2
counter = 3
for i in range(2,number+1):
    n3 = n1 + n2
    if n3 <= number and n3 >0:
        print(str(n3) + " ")
        arr1[counter+1] = n3
    if n3 == number:
        break
    n1 = n2
    n2 = n3
print("\n\nFab after inserting value : ")
print(str(arr1[0]) + " " + str(arr1[1])+ " ")
counter = 2
for y in range(2,len(arr1)):
    if  arr1[y] == 0:
        break
    print(arr1[y] + " ")
    counter+=1
for c in range(0,counter):
    m =0
    flag = 0
    m = arr1[c]/2
    for j in range(2, int(m+2)):
        if arr1[c]% j ==0:
            FinalState[c] = arr1[c]
            flag =1
            break
if flag==0:
    if arr1[c] >=2:
        arr2[c] = arr1[c]
    else:
        FinalState[c]= arr1[c]
print("\n\n Prime numbers :")
for y in range(2,len(arr2)):
    if arr2[y] == 0 :
        continue
    print(arr2[y]+ " ")
print("\n\n After deleting prime numbers!!")
print("Final State :")
print(str(FinalState[0]) + " " + str(FinalState[1]) + " ")
for y in range(2,len(FinalState)):
    if FinalState[y]==0:
        continue
    print(FinalState[y]+ " ")