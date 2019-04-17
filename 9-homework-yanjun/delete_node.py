import logging
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='my.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s  - %(message)s')


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

    def print_node(self, node):
        res_list = []
        while node:
            res_list.append(str(node.val))
            node = node.next
        logging.info('->'.join(res_list))


if __name__ == '__main__':
    node1 = ListNode(4)
    node2 = ListNode(5)
    node3 = ListNode(1)
    node4 = ListNode(9)
    node5 = ListNode(13)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    calc = Solution()
    calc.print_node(node1)
    calc.deleteNode(node2)
    calc.print_node(node1)
