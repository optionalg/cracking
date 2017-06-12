"""
Chapter 3: Stacks and Queues
"""

class ThreeOne(object):
    """ Question 1

    Describe how you could use a single array to implement three stacks.
    """
    
    maxStacks = 3

    def __init__(self, size):
        self.maxCapacity = size
        self.arr = [None] * size * 3
        self.sizes = [0, 0, 0]

    def isFull(self, which):
        if self.sizes[which] > self.maxCapacity / 3:
            return True
        return False

    def isEmpty(self, which):
        if self.sizes[which] == 0:
            return True
        return False

    def push(self, which, data):
        if isFull(which):
            raise ValueError('stack {} is full'.format(which))

        self.sizes[which] += 1
        index = which * (self.maxCapacity / 3) + self.sizes[which]
        self.arr[index] = data

    def pop(self, which):
        if isEmpty(which):
            raise ValueError('stack {} is empty'.format(which))

        index = which * (self.maxCapacity / 3) + self.sizes[which]
        value = self.arr[index]
        self.arr[index] = None
        self.sizes[which] -= 1
        return value

    def peek(self, which):
        if isEmpty(which):
            raise ValueError('stack {} is empty'.format(which))

        index = which * (self.maxCapacity / 3) + self.sizes[which]
        return self.arr[index]

class MinQueue(object):
    """ Question 2

    How would you design a stack which, in addition to push and pop has a
    function min which returns the minimum element? They all operate in O(n)
    time.
    """

    def __init__(self):
        self.stack = deque()
        self.mins = deque()

    def push(self, data):
        if data < self.peekMin():
            self.mins.append(data)
        self.stack.append(data)

    def pop(self):
        val = self.stack.pop()
        if val == self.peekMin():
            self.mins.pop()
        return val

    def peekMin(self):
        return self.mins.peek()

class SetOfStacks(object):
    """ Question3

    Implement a SetOfStacks composed of several stacks and should create a new
    stack once the previous one exceeds capacity.
    """

    def __init__(self, maxSize=30):
        self.maxSize = maxSize
        self.stacks = [deque()]
        self.index = 0

    def push(self, data):
        if len(self.stacks[index]) == self.maxSize:
            self.stacks.append(deque)
            self.index += 1
        self.stacks[index].append(data)

    def pop(self):
        val = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks = self.stacks[:index]
            self.index -= 1
        return val

    def peek(self):
        return self.stacks[index].peek()

    def popAt(self, index):
        val = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks = self.stacks[:index] + self.stacks[index+1:]
        return val

class MyQueue(object):
    """ Question 4

    Implement a MyQueue class which implements a queue using two stacks.
    WHYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
    """

    ### wellllllllll, python doesn't have dedicated stacks and queues.....
    def __init__(self):
        self.old = deque()
        self.new = deque()

    def push(self, data):
        self.new.append(data)

    def pop():
        if not self.old:
            while self.new:
                self.old.append(self.new.pop())
        return self.old.pop()

    def peek():
        if not self.old:
            while self.new:
                self.old.append(self.new.pop())
        return self.old.peek()

def sortStack(stack):
    """ Question 5

    Write a program to sort a stack such that the smallest items are on the top.
    You can use an additional temporary stack, but you may not copy the elements
    into any other data structure. The stack supports the following operations:
    push, pop, peek, isEmpty.
    """

    buff = deque()
    while not stack.isEmpty():
        temp = stack.pop()
        while not buff.isEmpty() and buff.peek() > temp:
            stack.append(buff.pop())
        buff.push(temp)
        while not buff.isEmpty():
            stack.append(buff.pop()) 
    return stack

class AnimalQueue(object):
    """ Question 6

    A shelter for dogs and cats operates on a FIFO basis. People can adopt the
    oldest, the oldest dog, or the oldest cat.
    """

    class Animal(object):

        def __init__(self, kind):
            self.kind = kind

    def __init__(self):
        self.total = 0
        self.cats = deque()
        self.dogs = deque()

    def enqueue(self, mutt):
        if mutt.kind = 'dog':
            self.dogs.append((mutt, self.index))
        else:
            self.cats.append((mutt, self.index))
        self.index += 1

    def dequeueAny(self):
        if self.cats.peek()[1] < self.dogs.peek()[1]:
            return self.cats.popleft()
        else:
            return self.dogs.popleft()

    def dequeueCat(self):
        return self.cats.popleft()

    def dequeueDog(self):
        return self.dogs.popleft()

    
