class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    res = dummy
    carry = 0

    while l1 or l2 or carry:
        total = carry

        if l1:
            total += l1.val
            l1 = l1.next

        if l2:
            total += l2.val
            l2 = l2.next

        carry = total // 10
        num = total % 10

        new_node = ListNode(num)
        res.next = new_node
        res = res.next

    return dummy.next

def createLinkedList():
    n = int(input("Enter the number of elements: "))
    print("Enter the elements: ")
    head = None
    temp = None
    for _ in range(n):
        val = int(input())
        new_node = ListNode(val)
        if not head:
            head = new_node
            temp = head
        else:
            temp.next = new_node
            temp = temp.next
    return head

def printLinkedList(head):
    while head:
        print(head.val)
        head = head.next
    print()

def main():
    l1 = createLinkedList()
    l2 = createLinkedList()

    result = addTwoNumbers(l1, l2)

    print("The sum of the two numbers is: ")
    printLinkedList(result)

if __name__ == "__main__":
    main()
