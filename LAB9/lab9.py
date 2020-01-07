from numpy import array
# from IPython.display import clear_output
# STACK

# def Push( Arr, Top, Maxstk, Value):
#     if Top == Maxstk-1:
#         print("stack full")
#     else:
#         Top[0] +=1
#         Arr[Top[0]] = Value
#
#
# def Pop (Arr , Top):
#     if Top[0]==-1:
#         print("stack full")
#     else:
#         Value = Arr[Top[0]]
#         Top[0] -=1a
#     return Value
#
#
# def peak (Arr, Top):
#     print(Arr[Top[0]])
#     return Value
#
# Top = [-1]
# Maxstk = 5
#
# Arr = array([0 for i in range(0, Maxstk)])
#
# Value = int(input("inster value"))
# Push(Arr,Top,Maxstk,Value)
#
#
#
#
#
# Value = int(input("inster value"))
# Push(Arr,Top,Maxstk,Value)
#
# Value = int(input("inster value"))
# Push(Arr,Top,Maxstk,Value)
#
#
# print(str(Pop(Arr,Top)) + " is remove ")
# for i in range(0,Top[0] + 1):
#     print(Arr[i], end=" ")
#
# print(str(peak(Arr,Top))+"peak value")

class Stack:
    def __init__(self, size):
        self.Top = -1
        self.MAXSTK = size
        self.Arr = array([0 for i in range(0, self.MAXSTK)])

    def IsFull(self):
        if self.Top == self.MAXSTK - 1:
            return  True
        else:
            return False

    def Isempty(self):
        if self.Top == - 1:
            return True
        else:
            return False

    def Push(self , value):
        if self.IsFull():
            print("stack is full")
        else:
            self.Top +=1
            self.Arr[self.Top] = value
    def Pop(self):
        if self.Isempty():
            print("stack is empty")
        else:
            value = self.Arr[self.Top]
            self.Top -=  1
        return value

    def PRINT(self):
        if self.Isempty():
            print("stack is empty")

        else:
            for i in range(0, self.Top):
                print(self.Arr[i],end=" ")

    def PEEK(self):
        if self.Isempty():
            print("stack is empty")

        else:
            return self.Arr[self.Top]










MYSTACK = Stack(10)
# MYSTACK.Push(12)
# MYSTACK.Push(23)
# MYSTACK.PRINT()

while True:
    print("1 for insert")
    print("2 for delte")
    print("3 peak value")
    print("4 stack size")
    print("5 print stack")
    print("6 close")

    choise = int(input("<"))
    # from IPython.display import clear_output
    # clear_output()
    if choise == 1:
        MYSTACK.Push(int(input("enter value:")))
        # clear_output()
    elif choise == 2:
        print(str(MYSTACK.Pop()) + " Value Remove")
    elif choise == 3:
        print(str(MYSTACK.PEEK()) + " is top value")
    elif choise == 4:
        print(str(MYSTACK.Top) + " current size of stack")
    elif choise == 5:
        MYSTACK.PRINT()
    elif choise == 6:
        break
    else:
        print("invalid choice")


