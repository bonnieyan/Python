'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    #这里不需要做递归 时间复杂度比较高
    #可以考虑用遍历方式去实现
    #具体算法参考归并排序
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def print_node(self, node):
        res_list = []
        while node:
            res_list.append(str(node.val))
            node = node.next
        print('->'.join(res_list))


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3
    l1 = node1
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(4)
    node_1.next = node_2
    node_2.next = node_3
    l2 = node_1
    cal = Solution()
    res = cal.mergeTwoLists(l1, l2)
    cal.print_node(res)