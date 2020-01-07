class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
class tree:

    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            ptr = self.root
            while self.root !=None:
                if value <= ptr.data:
                    if ptr.left is None:
                        ptr.left = Node(value)
                        break
                    else:
                        ptr = ptr.left
                elif value > ptr.data:

                    if ptr.right is None:
                        ptr.right =  Node(value)
                        break
                    else:
                        ptr = ptr.right

    def inoder(self,ptr):
        if ptr is not None:
            self.inoder(ptr.left)
            print(ptr.data)
            self.inoder(ptr.right)

    def preoder(self,ptr):
        if ptr is not None:
            print(ptr.data)
            self.preoder(ptr.left)
            self.preoder(ptr.right)
    def postoder(self,ptr):
        if ptr is not None:
            self.postoder(ptr.left)
            self.postoder(ptr.right)
            print(ptr.data)
    def descoder(self, ptr):
        if ptr is not None:
            self.descoder(ptr.right)
            print(ptr.data)
            self.descoder(ptr.left)
    # level oder treverse start
    def printLevelOrder(self,root):
        h = self.height(root)
        for i in range(1, h + 1):
            self.printGivenLevel(root, i)

    def printGivenLevel(self,root, level):
        if root is None:
            return
        if level == 1:
            print(root.data)
        elif level > 1:
            self.printGivenLevel(root.left, level - 1)
            self.printGivenLevel(root.right, level - 1)

    def height(self,node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            # Use the larger one
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
    #         end travel oder traverse

    def find_highest_value(self, root):
        # find a max value in a tree
        if root.right is not None:
            return self.find_highest_value(root.right)

        return root

    def lowest_value(self,root):
        if root.left is not None:
            return self.lowest_value(root.left)
        return root


mytree = tree()
mytree.insert(50)
mytree.insert(40)
mytree.insert(35)
mytree.insert(60)
mytree.insert(55)
mytree.insert(45)
mytree.insert(65)
print("inoder")
mytree.inoder(mytree.root)
print("preoder")
mytree.preoder(mytree.root)
print("postoder")
mytree.postoder(mytree.root)
print("decending oder")
mytree.descoder(mytree.root)
print("level oder traverse")
mytree.printLevelOrder(mytree.root)
re = mytree.find_highest_value(mytree.root)
print("highest value: ",re.data)
re1 = mytree.lowest_value(mytree.root)
print("lowest value: ",re1.data)
