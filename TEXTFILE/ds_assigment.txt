# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.left = None
#         self.right = None
#
# def findpresuc(root,key):
#
#     if root is None:
#         return
#     if root.key == key:
#         if root.left is not None:
#             temp = root.left
#             while(temp.right):
#                 temp = temp.right
#             # findpresuc(temp)
#             findpresuc.pre = temp
#         if root.right is not None:
#             temp = root.right
#             while temp.left:
#                 temp  = temp.left
#             # findpresuc(temp)
#             findpresuc.suc = temp
#         return
#     if root.key > key:
#         findpresuc.suc = root
#         findpresuc(root.left,key)
#     else:
#         findpresuc.pre = root
#         findpresuc(root.right,key)
# def insert(node,key):
#     if node is None:
#         return Node(key)
#     if key < node.key:
#         node.left = insert(node.left,key)
#     else:
#         node.right = insert(node.right,key)
#     return node
#
# root = None
# root = insert(root,50)
# insert(root,48)
# insert(root,30)
# insert(root,20)
# insert(root,15)
# insert(root,25)
# insert(root,32)
# insert(root,31)
# insert(root,35)
# insert(root,70)
# insert(root,65)
# insert(root,67)
# insert(root,66)
# insert(root,69)
# insert(root,90)
# insert(root,98)
# insert(root,94)
# insert(root,99)
#
# findpresuc.pre = None
# findpresuc.suc = None
#
# findpresuc(root,key=30)
#
# if findpresuc.pre is not None:
#     print("predecessor is:" , findpresuc.pre.key)
# else:
#     print("no predecessor")
# if findpresuc.suc is not None:
#     print("successor is:", findpresuc.suc.key)
# else:
#     print("no successor")
#
#

# python 3


""" Python3 code for inorder succesor
and predecessor of tree """


# A Binary Tree Node
# Utility function to create a new tree node
class getnode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""  
since inorder traversal results in  
ascendingorder visit to node , we  
can store the values of the largest  
o which is smaller than a (predecessor)  
and smallest no which is large than  
a (succesor) using inorder traversal  
"""


def find_p_s(root, a, p, q):
    # If root is None return
    if (not root):
        return

    # traverse the left subtree
    find_p_s(root.left, a, p, q)

    # root data is greater than a
    if (root and root.data > a):

        # q stores the node whose data is greater
        # than a and is smaller than the previously
        # stored data in *q which is sucessor
        if ((not q[0]) or q[0] and
                q[0].data > root.data):
            q[0] = root

            # if the root data is smaller than
    # store it in p which is predecessor
    elif (root and root.data < a):
        p[0] = root

        # traverse the right subtree
    find_p_s(root.right, a, p, q)


# Driver Code
if __name__ == '__main__':

    root1 = getnode(50)
    root1.left = getnode(48)
    root1.right = getnode(70)
    root1.left.left = getnode(30)
    root1.left.left = getnode(20)
    root1.left.right = getnode(32)
    root1.left.left = getnode(15)
    root1.left.right = getnode(25)
    root1.left.left = getnode(31)
    root1.left.left = getnode(35)
    # root1.left.right = getnode(30)
    root1.right.left = getnode(65)
    root1.right.right = getnode(90)
    root1.left.right = getnode(67)
    root1.right.right = getnode(98)
    root1.right.right = getnode(66)
    root1.left.right = getnode(69)
    root1.right.right = getnode(99)
    root1.right.left = getnode(94)

    p = [None]
    q = [None]

    find_p_s(root1, 98, p, q)

    if (p[0]):
        print(p[0].data, end="")
    if (q[0]):
        print("", q[0].data)



























