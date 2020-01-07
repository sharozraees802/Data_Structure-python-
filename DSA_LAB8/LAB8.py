class Node:

    def __init__(self, value):
        self.info = value
        self.Next = None
        self.prev = None

    def Print(self):
        print(self.info)
        # if self.Next != Node:
        if self.Next is not None:
            self.Next.Print()

class LinkedList:

    def __init__(self):
        self.Start = None

    def __int__(self, value):
        self.Start = Node(value)

    def InsertOnEnd(self, value):

        if self.Start is None:
            self.Start = Node(value)

        else:
            ptr = self.Start
            while ptr.Next != None:
                ptr = ptr.Next
            ptr.Next = Node(value)




    def count(self):
        if self.Start is None:
            print("list empty")
        else:
            ptr = self.Start
            count = 1
            while ptr.Next != None:

                count += 1
                ptr = ptr.Next
            return count

    def InsertionOnPosition(self,pos, value):
        if(self.Start is None):
            print("List is Empty")
        elif (pos < 0 and pos >= self.count()):


            ptr = self.Start
            for i in range(1 , pos-1):
                ptr = ptr.Next
            New = Node(value)
            New.Next = ptr.Next
            ptr.Next = New
        else:
            print("position Doesnot Exist")

    def DeleteFormEnd(self):
        if self.Start == None:
            print("List is already Empty")
        elif self.Start.Next == None:
            self.Start=None
        else:
            ptr = self.Start
            while ptr.Next.Next != None:
                ptr = ptr.Next
            ptr.Next = None


    def DeleteFormBeing(self):
        if self.Start is None:
            print("List is already Empty")
        else:
            self.Start == self.Start.Next


    def Seach(self,FindValue):

        if self.Start is None:
            print("List empty")
        else:
            ptr = self.Start
            count = 1
            Flag = False
            while ptr.Next != None:
                if ptr.info == FindValue:
                    Flag = True
                    break
                count +=1
                ptr = ptr.Next

        if (Flag):
            print("VAlue found on position " + str(count))
        else:
            print("not found")

    def print(self):
        if self.Start ==None:
            print("list is empty")
        else:
            self.Start.Print()






#MAIN

# start = Node(12)
# start.Next = Node(13)
# start.Next.Next = Node(14)
# start.Next.Next.Next = Node(15)
#
# start.print()

mylist = LinkedList()

mylist.InsertOnEnd(13)
mylist.InsertOnEnd(14)
mylist.InsertOnEnd(15)
mylist.InsertOnEnd(16)
mylist.print()

print()
print(mylist.count())

print("position me aad")

mylist.InsertionOnPosition(3,44)

mylist.print()
print("delete last")


# mylist.DeleteFormEnd()
# mylist.DeleteFormEnd()

mylist.print()

print("beging delete")

# mylist.DeleteFormBeing()
mylist.print()


mylist.Seach(15)