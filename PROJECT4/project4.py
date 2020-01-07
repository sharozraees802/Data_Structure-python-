from numpy import array
# answer = ""
# result = ""
# answer = input("inpute a number")
#
# num = int(answer)
# while num > 1 :
#     rem = num%2
#     s = str(rem)
#     result = s + result
#     num /=2
# result  = str(num) + result
#
# print(result)



#
# Arr = [3,1,2]
# # Arr = array([0 for i in range(0, 8)])
# n = int(input("enter a number"))
#
# for i in range(0,n):
#     Arr[i] = int(n %2)
#     n =n/2
# print("binary number")
#
# for i in range(0,i-1):
#     print(Arr[i],end="")




number = int(input('Enter decimal number: '))
temp = ''
while True:
    if number > 0:
        temp += str(number % 2)
        number = number // 2
    else:
        break
result = ''
for i in range(len(temp)-1, -1, -1):
    result += temp[i]
print('In binary format: ', result)