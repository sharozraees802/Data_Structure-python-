f = open('myfile.txt' , 'r')

for l in range(0,8):
   arr = []

   for i in range(1,5):
       f1 = int(f.readline())
       arr.append(f1)

   num = arr[0]
   num1 = arr[1]
   power = 0
   deci = 0
   deci1 = 0
   res = 0
   address = arr[2]
   print()


   while(num != 0):
       dig = num%10
       deci = deci + (dig*2**power)
       power += 1
       num = num//10
   power = 0
   while(num1 != 0):
       dig1 = num1%10
       deci1 = deci1 + (dig1*2**power)
       power += 1
       num1 = num1//10
   print()
   print("After changing it to Decimal")



   print()
   opr = str(arr[3])
   arr = [deci,deci1,address,opr]
   print(arr)
   if opr == "0":
       res = deci+deci1
       print("After Addition: " , res)
   elif opr == "1":
       res = deci-deci1
       print("After Subtraction: " , res)
   elif opr == "2":
       res = deci*deci1
       print("After Multiplication: " , res)
   elif opr == "3":
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


       arr = [deci,deci1,string,opr]
       print(arr)
       print("---------------------------------")

   elif(res >= 0):
       while (res != 0):
           a = res%2
           string += str(a)
           res = res//2
       s = string
       string = ""
       for i in range(len(s)-1,-1,-1):
           string += s[i]

       arr = [deci,deci1,string,opr]
       print(arr)
       print("---------------------------------")
f.close()
