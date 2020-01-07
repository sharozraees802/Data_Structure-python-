# class Node(object):
#     def __init__(self):
#         self.data = None  # contains the data
#         self.next = None  # contains the reference to the next node
# class LinkedList:
#     def __init__(self):
#         self.cur_node = None
#         self.count=0
#         self.file = open('faiq.txt', 'a+')
#         self.arr=[]
#         self.get=False
#
#     def add_node(self, data):
#         new_node = Node()
#         new_node.data = data
#         new_node.next = self.cur_node
#         self.cur_node = new_node
#         self.count+=1
#         self.arr.append(data)
#         if self.count>=10 and self.get is False:
#             self.file_input()
#             self.get=True
#     def file_input(self):
#         for i in range(self.count):
#             self.file.write(str(self.arr[i])+'\n')
#     def list_print(self):
#         node = self.cur_node
#         while node:
#             print(node.data)
#             node = node.next
#
#     def search(self,val):
#         node = self.cur_node
#         while node:
#             if  node.data==val:
#                 print('found')
#                 print(node.data)
#             node = node.next
#
#
#
# ll = LinkedList()
#
#
#
# ll.search(5)
# for i in range(12):
#     ll.add_node(i)
#
#
#


import os
class Node(object):
    def __init__(self):
        self.data = None  # contains the data
        self.next = None  # contains the reference to the next node
class LinkedList:
    def __init__(self):
        self.cur_node = None
        self.count=0
        with open('text.txt') as self.file:
            self.file.seek(0, os.SEEK_END)  # go to end of file
            if self.file.tell():  # if current position is truish (i.e != 0)
                self.file.seek(0)  # rewind the file for later use
            else:
                print("file is empty")
                f=open('text.txt','w')
                f.write('')
        self.file=open('text.txt','w')
        self.arr=[]
        self.get=False

    def add_node(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.cur_node
        self.cur_node = new_node
        self.count+=1
        self.arr.append(data)
        if self.count>=10 and self.get is False:
            self.file_input()
            self.get=True
    def file_input(self):
        for i in range(self.count):
            self.file.write(str(self.arr[i])+'\n')
    def list_print(self):
        node = self.cur_node
        while node:
            print(node.data)
            node = node.next

    def search(self,val):
        node = self.cur_node
        while node:
            if  node.data==val:
                print('found')
                print(node.data)
            node = node.next



ll = LinkedList()



ll.search(5)
for i in range(10,25):
    ll.add_node(i)




