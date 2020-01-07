class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:

            ptr = self.root
            while True:
                if value <= ptr.data:
                    if ptr.left == None:
                        ptr.left = Node(value)
                        break
                    else:
                        ptr = ptr.left
                elif value > ptr.data:
                    if ptr.right is None:
                        ptr.right = Node(value)
                        break
                    else:
                        ptr = ptr.right

    def inoder(self, ptr):
        if ptr != None:
            self.inoder(ptr.left)
            print(ptr.data)
            self.inoder(ptr.right)

    def preoder(self, ptr):
        if ptr != None:
            print(ptr.data)
            self.preoder(ptr.left)
            self.preoder(ptr.right)

    def postoder(self, ptr):
        if ptr != None:
            self.postoder(ptr.left)
            self.postoder(ptr.right)
            print(ptr.data)

    def descoder(self, ptr):
        if ptr != None:
            self.descoder(ptr.right)
            print(ptr.data)
            self.descoder(ptr.left)

    def find_highest_value(self,root):
        # find a max value in a tree
        if root.right != None:
            return self.find_highest_value(root.right)

        return root

    def find_lowest_value(self, root):
        # find a max value in a tree
        if root.left != None:
            return self.find_lowest_value(root.left)

        return root


    def delete(self, Ptr, value):
        if ptr is




mytree = Tree()
mytree.insert(50)
mytree.insert(40)
mytree.insert(35)
mytree.insert(60)
mytree.insert(55)
print("inoder")
mytree.inoder(mytree.root)
print("preoder")
mytree.preoder(mytree.root)
print("postoder")
mytree.postoder(mytree.root)
print("descoder")
mytree.descoder(mytree.root)
result = mytree.find_highest_value(mytree.root)
print("hight value: ",result.data)
result1 = mytree.find_lowest_value(mytree.root)
print("lowest value: ",result1.data)




# def main():
#     mytree = Tree()
#     mytree.insert(50)
#     mytree.insert(40)
#     mytree.insert(35)
#     mytree.insert(60)
#     mytree.insert(55)
#     print("inoder")
#     mytree.inoder(mytree.root)
#     print("preoder")
#     mytree.preoder(mytree.root)
#     print("postoder")
#     mytree.postoder(mytree.root)
#     print("descoder")
#     mytree.descoder(mytree.root)
#     result = mytree.find_highest_value(mytree.root)
#     print("hight value: ",result.data)
#     result1 = mytree.find_lowest_value(mytree.root)
#     print("lowest value: ",result1.data)
#
# if __name__ == "__main__":
#     main()