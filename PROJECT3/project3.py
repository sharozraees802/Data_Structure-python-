f = open('DATA_VALUE.txt' , 'r')

for l in range(0,8):
   arr = []

   for i in range(1,5):
       f1 = int(f.readline())
       arr.append(f1)


   number = arr[0]
   number1 = arr[1]
   power = 0
   decimal = 0
   decimal1 = 0
   result = 0
   address = arr[2]
   print()


   while number != 0:
       digit = number % 10
       decimal = decimal + (digit*2**power)
       power +=1
       number =  number//10
   power = 0


   while number1 != 0:
       digit1 = number1 % 10
       decimal1 = decimal1 + (digit1*2**power)
       power +=1
       number1  =  number1//10
   print()
   print("AFTER CHANGE  INTO DECIMAL")


   print()
   operation = str(arr[3])
   arr = [decimal,decimal1,address,operation]
   print(arr)
   if operation =="0":
       result =  decimal + decimal1
       print("After ADDITION:" , result)
   elif operation == "1":
       result = decimal - decimal1
       print("After SUBTRACTION:", result)
   elif operation =="2":
       result = decimal * decimal1
       print("After MULTIPLICATION:", result)
   elif operation =="3":
       result = int(decimal / decimal)
       print("After DIVISION:", result)
   print()



   string = ""
   if result < 0:
       result = -(result)
       while result != 0:
           a = result % 2
           string += str(a)
           result = result//2
       s = string
       string = ""
       for i in range(len(s)-1,-1,-1):
           string += s[i]

       arr = [decimal,decimal1,string,operation]
       print(arr)
       print("--------------------------------------------------")




f.close()








# num = int(input("Enter a Number in Binary: "))
# num1 = int(input("Enter a Number in Binary: "))
# power = 0
# deci = 0
# deci1 = 0
# res = 0


# num = arr[0]
# num1 = arr[1]
# power = 0
# deci = 0
# deci1 = 0
# res = 0
# address = arr[2]
# print()
#
# address = int(input("Enter Address where you want to put the Results: "))
# print()
# arr = [num,num1,0,address]
# print(arr)
# while(num != 0):
#    dig = int(num%10)
#    deci = deci + (dig*2**power)
#    power += 1
#    num = int(num/10)
# power = 0
# while(num1 != 0):
#    dig1 = int(num1%10)
#    deci1 = deci1 + (dig1*2**power)
#    power += 1
#    num1 = int(num1/10)
# print()
# print("After changing it to Decimal")
# arr = [deci,deci1,0,address]
# print(arr)
# print()
# print("For Adiition Enter: 0000")
# print("For subtraction Enter: 0001")
# print("For Multiplication Enter: 0002")
# print("For Division Enter: 0003")
# print()
# opr = str(input("Enter your operation: "))
#
# if opr == "0000":
#    res = deci+deci1
#    print("After Addition: " , res)
# elif opr == "0001":
#    res = deci-deci1
#    print("After Subtraction: " , res)
# elif opr == "0002":
#    res = deci*deci1
#    print("After Multiplication: " , res)
# elif opr == "0003":
#    res = int(deci/deci1)
#    print("After Division: " , res)
#
# print()
#
#
# string = ""
#
# if res < 0:
#    res = -(res)
#    while (res != 0):
#        a = res%2
#        string += str(a)
#        res = res//2
#    s = string
#    string = ""
#    for i in range(len(s)-1,-1,-1):
#        string += s[i]
#
#    s = ""
#    for k in range(len(string)-1,-1,-1):
#        if string[k] == 1:
#            s = string.split(string[k],len(string)-1)
#
#    for m in range(0,len(string)):
#        if string[m] == 0:
#            string[m] = "1"
#        elif string[m] == 1:
#            string[m] = "0"
#
#    string = string + s
#    arr = [deci,deci1,opr,string]
#    print(arr)
#
#
# elif(res > 0):
#    while (res != 0):
#        a = res%2
#        string += str(a)
#        res = res//2
#    s = string
#    string = ""
#    for i in range(len(s)-1,-1,-1):
#        string += s[i]
#
#    arr = [deci,deci1,opr,string]
#    print(arr)