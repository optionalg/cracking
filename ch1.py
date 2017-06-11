from collections import Counter

"""
Chapter 1: Arrays and Strings
"""

def counter(string):
    """ Note on Counter:

    I use the Counter class here a lot. If the interview doesn't allow it,
    write a helper function that goes something like this:
    """
    
    toReturn = {}
    for char in string:
        if toReturn.get(char):
            toReturn[char] += 1
        else:
            toReturn[char] = 1
    return toReturn

def is_unique(string):
    """ Question 1, Part 1

    Implement an algorithm to determin if a string has all unique characters.
    """
    ### Counter throws all the characters of string into a dictionary and
    ### counts the instances of each character
    count = Counter(string)
    for c in count.items():
        if c[1] > 1:
            return False
    return True

def is_unique_nomem(string):
    """ Question 1, Part 2

    What if you cannot use additional data structures?
    """

    ### With no additional data structures, we don't have a choice but to
    ### use the O(n^2) method of comparing each character to each subsequent
    ### character. We can assume that all the previous characters are unique.

    ### Note: if sorting is considered without additional data structures, then
    ### an O(nlogn) solution is to sort, then compare consecutive characters.
    """
    string = sorted(string)
    n = len(string)
    for i in xrange(n):
        if string[i] == string[i+1]:
            return False
    return True
    """
    n = len(string)
    for i in xrange(n):
        for j in xrange(i, n):
            if string[i] == string[j]:
                return False
    return True

def check_perm(s1, s2):
    """ Question 2

    Given two strings, write a method to decide if one is a permuation of the
    other.
    """
    
    if len(s1) != len(s2):
        return False
    
    ### O(n) solution is to dump both into counters and compare the two.
    count = Counter(s1)
    for char in s2:
        if not count[char]:
            return False
        count[char] -= 1
    return True

def urlify(string, tlen):
    """ Question 3

    Write a method to replace all spaces in a string with "%20". You may assume
    that the string has sufficient space at the end to hold the additional
    characters, and that you are given the "true" length of the string. Perform
    this operation in-place.
    """

    ### I mean, in Python we can just use the str.replace() method... but I
    ### don't think that's valid here. The in-place restriction is just for
    ### other language that require using arrays of chars instead of string
    ### objects. We can pretend that we're given a list of chars here to mimic
    ### that restriction.

    ### If you want to do something like this in-place, it's best to start 
    ### from the back.

    llen = len(string) - 1
    for i in xrange(tlen-1, -1, -1):
        charAt = string[i]
        if charAt != ' ':
            string[llen] = '0'
            string[llen-1] = '2'
            string[llen-2] = '%'
            llen -= 3
        else:
            string[llen] = charAt
            llen -= 1
    return ''.join(string)

def palin_perm(string):
    """ Question 4

    Given a string, write a function to check if it is a permutation of a
    palindrome.
    """

    ### Some ambiguity here: the book treats whitespace as if it doesn't exist.
    ### I'm gonna stick to that then. The book also ignores case. Either way,
    ### the basic principle is, dump into a Counter, and check that there is at
    ### most one character that has an odd count.

    count = Counter(string.lower())
    odd = 0
    for char, num in count.items():
        if char:
            if num % 2 == 1:
                if odd:
                    return False
                else:
                    odd = 1
    return True
        
def one_away(s1, s2):
    """ Question 5

    Given two strings, write a function to check if they are at most one edit
    away from each other.
    """

    ### Insertion and deletion are essentially the same thing.
    def insdel(first, second):
        ### first is shorter than the second
        i1 = 0
        i2 = 0
        while i1 < len(first) and i2 < len(second):
            if first[i1] != second[i2]:
                if i1 != i2:
                    return False
            else:
                i1 += 1
                i2 += 1
        return True

    def replac(first, second):
        diffs = 0
        for i in xrange(len(first)):
            if first[i] != second[i]:
                if diffs:
                    return False
                diffs += 1
        return True

    l1 = len(s1)
    l2 = len(s2)
    if l1 == l2:
        return replac(s1, s2)
    elif l1 + 1 == l2:
        return insdel(s1, s2)
    elif l1 == l2 + 1:
        return insdel(s2, s1)
    return False

def str_compress(string):
    """ Question 6

    Implement a method to perform basic string compression using the counts of
    repeated characters. If the compressed string is larger than the original,
    return the original string. You can assume the string has only upper and
    lowercase letters.
    """

    toReturn = []
    look = string[0]
    index = 1
    count = 1
    while index < len(string)-1:
        if string[index] == look:
            count += 1
            index += 1
        else:
            toReturn.append(string[index-1] + str(count))
            count = 1
            look = string[index]
            index += 1
    toReturn = ''.join(toReturn)
    return toReturn if len(toReturn) < len(string) else string

def rotate(matrix):
    """ Question 7

    Rotate an NxN matrix 90 degrees clockwise in-place.
    """

    if not matrix or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)
    for layer in range(n/2):
        ### layer defines the row we're working on.
        ### to get the column, we iterate over the row itself.
        top = layer
        bot = n - layer - 1
        for i in range(top, bot):
            offset = i - top
            temp = matrix[top][i]
            matrix[top][i] = matrix[bot-offset][top]
            matrix[bot-offset][top] = matrix[bot][bot-offset]
            matrix[bot][bot-offset] = matrix[i][bot]
            matrix[i][top] = temp

    return matrix

def zeromat(matrix):
    """ Question 8

    Write an algorithm such that if an element in an MxN matrix is 0, its
    entire row and column are set to 0
    """

    n = len(matrix)
    m = len(matrix[0])
    rows = []
    cols = []
    for row in xrange(n):
        for col in xrange(m):
            if matrix[row][col] == 0:
                rows.append(row)
                cols.append(col)

    for row in rows:
        matrix[thing] = [0] * m
    for col in cols:
        for i in xrange(n):
            matrix[i][col] = 0

    return matrix

def strrotate(s1, s2):
    """ Question 9

    Given two strings, s1 and s2, write code to check if s2 is a rotation of s1
    using only one call to isSubstring().
    """

    def isSubstring(s1, s2):
        return True if s1.find(s2) != -1 else False
    
    return isSubstring(s1+s1, s2) if len(s1) == len(s2) else False
    
