class btree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def isSibling(root, first, second):

        if root == None:
            return 0
        return (
            (root.left == first and root.right == second) or
            (root.left == second and root.right == first) or
            isSibling(root.left, first, second) or
            isSibling(root.right, first, second)
         )

    def curlevel(root, first, level):
        if root == None:
            return 0
        if root == first:
            return level

        templevel = curlevel(root.left, first, level+1)
        if templevel != 0:
            return templevel

        return curlevel(root.right, first, level +1)

    def isCousin(self, root, first, second):
        if ((curlevel(root,first,1) == curlevel(root, second, 1)) and
            not (isSibling(root, first, second))):
            return True
        else:
            return False


    root = btree(1)
    root.left = btree(2)
    root.right = btree(3)
    root.left.left = btree(4)
    print(isCousin(root, 3,4))
