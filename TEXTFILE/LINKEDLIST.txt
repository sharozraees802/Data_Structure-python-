class Node:

    def __init__(self, value):
        self.info = value
        self.Next = None

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

    def InsertatBegin(self, value):
        if self.Start==None:
            self.Start = Node(value)
        else:
            temp = Node(value)
            temp.Next = self.Start
            self.Start  = temp

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
mylist.InsertatBegin(23)
mylist.InsertOnEnd(13)
mylist.InsertOnEnd(14)
mylist.InsertOnEnd(15)
mylist.InsertOnEnd(16)
mylist.print()

