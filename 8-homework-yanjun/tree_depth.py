class node():
    def __init__(self, k=None, l=None, r=None):
        self.val = k
        self.left = l
        self.right = r


#这里可以不用递归实现 做一遍遍历就行了 
def listcreattree(root, llist, i):
    if i < len(llist):
        if llist[i] == 'null':
            return None  ###这里的return很重要
        else:
            root = node(k=llist[i])
            # print(llist[i])
            root.left = listcreattree(root.left, llist, 2 * i + 1)
            root.right = listcreattree(root.right, llist, 2 * i + 2)
            return root  ###这里的return很重要
    return root


def tree_depth(root):
    if root == None:
        return 0
    #最大深度
    return max(tree_depth(root.left), tree_depth(root.right)) + 1
    # return min(tree_depth(root.left), tree_depth(root.right)) + 1 最小深度


if __name__ == '__main__':
    root = node()
    # llist = ['1', '2', '3', '#', '4', '5']
    llist = [3, 9, 20, 'null', 'null', 15, 7]
    root = listcreattree(root, llist, 0)
    result = tree_depth(root)
    print(result)
