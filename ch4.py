from collections import deque

"""
Chapter 4: Trees and Graphs
"""

"""
Traversals
"""

def inOrder(root):
    """
    Visits nodes in sorted order (in a BST).
    """
    if root:
        inOrder(root.left)
        visit(root)
        inOrder(root.right)

def preOrder(root):
    """
    Visits the root first.
    """
    if root:
        visit(root)
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    """
    Visits the root last.
    """
    if root:
        postOrder(root.left)
        postOrder(root.right)
        visit(root)

def route(root, node):
    """ Question 1

    Given a directed graph, design an algorithm to find out whether there is a
    route between two nodes.
    """

    ### Just DFS it?

    if not root or not node:
        return False

    def dfs(root, node):
        root.visit()
        for neighbor in root.neighbors:
            if neighbor == node:
                return True
            dfs(neighbor, node)
        return False

    return dfs(root, node)

def min_tree(arr):
    """ Question 2

    Given a sorted (increasing order) array with unique integer elements, write
    an algorithm to create a binary search tree with minimal height.
    """

    n = len(arr)
    node = Node(arr[n/2])
    node.left = min_tree(arr[:n/2])
    node.right = min_tree(arr[n/2:])
    return node
    
def list_depths(root):
    """ Question 3

    Given a binary tree, design an algorithm which creates a linked list of all
    the nodes at each depth.
    """

    def helper(level, current):
        if not level:
            return current
        
        nextlevel = deque()
        toAppend = []
        while level:
            item = level.popleft()
            if item.left:
                nextlevel.append(item.left)
            if item.right:
                nextlevel.append(item.right)
            toAppend.append(item)

        return helper(nextlevel, current.append(toAppend))

    return helper(deque(root), [])

def check_balanced(root):
    """ Question 4

    Implement a function to check if a binary tree is balanced. For the purposes
    of this question, a balanced tree is defined to be a tree such that the
    heights of the two subtrees of any node never differ by more than one.
    """

    def check(root):
        if not root:
            return -1

        left = check_height(root.left)
        if left < -1:
            return -2

        right = check_height(root.right)
        if right < -1:
            return -2

        diff = left - right
        if abs(diff) > 1:
            return -1
        return max(left, right) + 1

    return False if check(root) < -1 else True

def validate_bst(root):
    """ Question 5

    Implement a function to check if a binary tree is a binary search tree.
    """

    def helper(root, mini, maxi):
        if not root:
            return True
        if root.data <= mini or root.data > maxi:
            return False
        if not helper(root.left, mini, root.data) or helper(root.right, root.data, maxi):
            return False
        return True

    return helper(root, -sys.maxint + 1, sys.maxint)

def successor(node):
    """ Question 6

    Write an algorithm to find the in-order successor of a given node.
    """

    ### If node has a right child, then return the leftmost child of node.right.
    ### Otherwise, we've finished looking at node's subtrees. If node was the
    ### left child of the parent, return parent.right's leftmost child.
    ### Otherwise, we need to find parent's parent until parent is not the right
    ### child.

    def leftmostchild(node):
        while node.left:
            node = node.left
        return node

    if not node:
        return None

    if not n.right:
        return leftmostchild(node)

    parent = node.parent
    while parent and parent.left is not node:
        node = parent
        parent = parent.parent

    return parent

def build_order(projects, dependencies):
    """ Question 7

    Find a build order that will allow the projects to be built. If none, return
    an error.

    Args:
        projects (list of str): Basically vertices in a graph.
        dependencies (list of tuples of str): Adjacency list of a directed graph
    """

    ### Need to do a topological sort.
    ### Get the indegree of each vertex
    index = {}
    for i in xrange(len(projects)):
        index[projects[i]] = i
    
    adjlist = {}
    for edge in dependencies:
        if adjlist.get(edge[0]):
            adjlist[edge[0]].append(edge[1])
        else:
            adjlist[edge[0]] = [edge[1]]
        
    projects = map(lambda thing: (thing, 0), projects)
    for edge in dependencies:
        idx = edge[1]
        projects[index[idx]][1] += 1

    sources = filter(lambda v: v[1] == 0, projects)
    if not sources:
        return None

    toReturn = []
    while sources:
        vertex = sources.pop()
        toReturn.append(vertex)
        for neighbor in adjlist.get(vertex):
            projects[index[neighbor]][1] -= 1
            if projects[index[neighbor]][1] == 0:
                sources.append(neighbor)
    if len(toReturn) == len(projects):
        return toReturn
    else:
        return None

def common_ancestor(node1, node2):
    """ Question 8

    Design an algorithm and write code to find the common ancestor of two nodes
    in a binary (not necessarily search) tree. Avoid using additional data
    structures.
    """

    h1 = 0
    h2 = 0
    t1 = node1
    t2 = node2
    while t1:
        t1 = t1.parent
        h1 += 1
    while t2:
        t2 = t2.parent
        h2 += 1

    if h1 > h2:
        for _ in xrange(h1-h2):
            node1 = node1.parent
    elif h2 > h1:
        for _ in xrange(h2-h1):
            node2 = node2.parent

    while (node1 is not node2) and node1.parent and node2.parent:
        node1 = node1.parent
        node2 = node2.parent

    return node1 if node1 is node2 else None

def common_ancestor_no_parent(node1, node2):
    
