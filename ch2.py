from collections import deque

"""
Chapter 2: Linked Lists
"""

class Node(object):

    """ Python translation of the Node class in the book.

    For the problems, I'm going to assume doubly linked if I need that power,
    unless the question demands a certain type. If I don't need the backwards
    link, I'm gonna be lazy and pretend it doesn't exist because of writing
    the extra lines.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        Node end = Node(data)
        Node head = self
        while head.next:
            head = head.next
        head.next = end

    def delete(head, data):
        look = head
        if look.data == data:
            return head.next

        while look.next:
            if look.next.data == data:
                look.next = look.next.next
                return head
            look = look.next

        return head

def remove_dups(head):
    """ Question 1

    Write code to remove duplicates from an unsorted linked list.
    """

    items = {}
    look = head
    while look.next:
        if items.get(look.data):
            look.next = look.next.next
        items[look.data] = 'lol'
        look = look.next

def remove_dups_nobuff(head):
    """ Question 1, part 2

    What if a temporary buffer is not allowed?
    """

    ### No choice but to do it quadratic style
    look = head
    while look:
        check = look.next
        while check.next:
            if check.data == look.data:
                check.next = check.next.next
        look = look.next

def kth_2_last(head):
    """ Question 2

    Implement an algorithm to return the kth to last element in a singly linked
    list.
    """

    ### Two ways:
    ### 1. Do it recursively and return when the stack reaches the right depth.
    ### 2. Iterate twice.
    ### 1 is faster if k > n/2, but 2 doesn't need extra memory.
    ### I like 2 because it's easy.

    count = 1
    look = head
    while look.next:
        look = look.next
        count += 1

    look = head
    for i in xrange(count-k):
        look = look.next
    return look.data

def delete_mid(node):
    """ Question 3

    Implement an algorithm to delete a node in the middle of a singly linked
    list, given only access to that node.
    """

    node.data = node.next.data
    node.next = node.next.next

def partition(head, x):
    """ Question 4

    Write code to partition a linked list around a value x, such that all nodes
    less than x come before all nodes greater than or equal to x. If x is
    contained within the list, the values of x only need to be after the
    elements less than x. The partition element x can appear anywhere in the
    right partition.
    """

    ### That last sentence makes this really easy.

    lefthead, lefttail, righthead, righttail = None, None, None, None
    look = head
    while look:
        if look.data < x:
            if not lefthead:
                lefthead = Node(look.data)
                lefttail = lefthead
            else:
                lefttail.next = Node(look.data)
                lefttail = lefttail.next
        else:
            if not righthead:
                righthead = Node(look.data)
                righttail = righthead
            else:
                righttail.next = Node(look.data)
                righttail = righttail.next
        look = look.next
    lefttail.next = righthead
    return lefthead

def sum_list(head1, head2, carry):
    """ Question 5

    You have two numbers represented by a linked list, where each node contains
    a single digit. The digits are stored in reverse order. Write a function
    that adds the two numbers and returns the sum as a linked list.
    """

    if not head1 and not head2 and not carry:
        return None

    toReturn = Node(0)
    val = carry
    if head1:
        val += head1.data
    if head2:
        val += head2.data
    toReturn.data = val % 10

    if head1 or head2:
        append = sum_list(None if not head1 else head1.next,
                          None if not head2 else head2.next,
                          val / 10)
        toReturn.next = append
    return toReturn

def sum_list_reverse(head1, head2):
    """ Question 5, part 2

    Suppose the digits are stored in forward order. Repeat the above problem.
    """

    def helper(head1, head2):
        ### Recurse
        sumlist = helper(head1.next, head2.next)
        ### sumlist[1] holds the carry value
        val = sumlist[1] + head1.data + head2.data
        newhead = Node(val % 10)
        newhead.next = sumlist[0]
        return (newhead, val / 10)

    def padding(head, length):
        for _ in xrange(length):
            pad = Node(0)
            pad.next = head
            head = pad
        return head

    l1 = length(head1)
    l2 = length(head2)

    if l1 < l2:
        head1 = padding(head1, l2-l1)
    else:
        head2 = padding(head2, l1-l2)


    sumlist = helper(head1, head2)

    if sumlist[1]:
        newhead = Node(sumlist[1])
        newhead.next = sumlist[0]
        return newhead
    else:
        return sumlist[0]

def palindrome(head):
    """ Question 6

    Implement a function to check if a linked list is a palindrome.
    """

    ### If the length of the list is unknown, then use a fast/slow iterator.
    ### When the fast iterator hits the end, the slow will be at the middle.
    fast = head
    slow = head
    ### Python doesn't have a stack class, per se.
    stack = deque()
    while fast and fast.next:
        stack.add(slow.data)
        slow = slow.next
        fast = fast.next.next

    ### This means the list has an odd number of elements
    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()
        if top != slow.data:
            return false
        slow = slow.next
    return True

def intersect(head1, head2):
    """ Question 7

    Given two singly linked lists, deter if the two lists intersect. Return the
    intersecting node. Intersection is defined by reference, not value.
    """

    ### We need a length method for lists.
    l1 = head1.length()
    l2 = head2.length()

    if l1 < l2:
        for _ in xrange(l2-l1):
            head2 = head2.next
    else:
        for _ in xrange(l1-l2):
            head1 = head1.next

    while head1.next:
        if head1 is head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    return None

def loops(head):
    """ Question 8

    Given a circular linked list, implement an algorithm that returns the node
    at the beginning of the loop.
    """

    ### The book has a nice proof of which node the two runners intersect at.
    ### TL;DR: If there are k nodes before the loop, the runners will meet up
    ### k nodes before the head of the loop.

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow = head
    while slow != head:
        slow = slow.next
        fast = fast.next

    return slow ## or fast doesn't matter

