
# decimalnumber = int(input("enter a first biinary number "))
# reminder =0
# result = None
# while(decimalnumber > 0):
#     reminder = decimalnumber %2
#     result= decimalnumber //2
#     print(result)
#     break





# num = int(input("entere a binary number"))
#
# print(bin(num))





# num = int(input("Enter a number: "))
# rem =0
# while  num >=1:
#     quot = num /2
#     rem += num%2
#
#
#     num = quot
# bin = " "
# i = len(rem)- 1
# while i >=0:
#     bin = bin + rem[i]
#     i -=1
# print(num)









































num = int(input("Enter a Number in Binary: "))
num1 = int(input("Enter a Number in Binary: "))
power = 0
deci = 0
deci1 = 0
res = 0
address = int(input("Enter Address where you want to put the Results: "))
print()
arr = [num,num1,0,address]
print(arr)
while(num != 0):
   dig = int(num%10)
   deci = deci + (dig*2**power)
   power += 1
   num = int(num/10)
   print("value of deci "+str(deci))
power = 0
while(num1 != 0):
   dig1 = int(num1%10)
   deci1 = deci1 + (dig1*2**power)
   power += 1
   num1 = int(num1/10)
print()
print("After changing it to Decimal")
arr = [deci,deci1,0,address]
print(arr)
print()
print("For Adiition Enter: 0000")
print("For subtraction Enter: 0001")
print("For Multiplication Enter: 0002")
print("For Division Enter: 0003")
print()
opr = str(input("Enter your operation: "))

if opr == "0000":
   res = deci+deci1
   print("After Addition: " , res)
elif opr == "0001":
   res = deci-deci1
   print("After Subtraction: " , res)
elif opr == "0002":
   res = deci*deci1
   print("After Multiplication: " , res)
elif opr == "0003":
   res = int(deci/deci1)
   print("After Division: " , res)

print()


string = ""

if res < 0:
   res = -(res)
   while (res != 0):
       a = res%2
       string += str(a)
       res = res//2
   s = string
   string = ""
   for i in range(len(s)-1,-1,-1):
       string += s[i]

   s = ""
   for k in range(len(string)-1,-1,-1):
       if string[k] == 1:
           s = string.split(string[k],len(string)-1)

   for m in range(0,len(string)):
       if string[m] == 0:
           string[m] = "1"
       elif string[m] == 1:
           string[m] = "0"

   string = string + s
   arr = [deci,deci1,opr,string]
   print(arr)


elif(res > 0):
   while (res != 0):
       a = res%2
       string += str(a)
       res = res//2
   s = string
   string = ""
   for i in range(len(s)-1,-1,-1):
       string += s[i]

   arr = [deci,deci1,opr,string]
   print(arr)