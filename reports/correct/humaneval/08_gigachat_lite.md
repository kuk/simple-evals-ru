# humaneval / gigachat-lite
### HumanEval/68
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
 </pre>
###### answer
<pre> ```python
def pluck(arr):
    # Initialize result list to store the smallest even value and its index
    result = []
    
    # Iterate through each element in the input array
    for i, num in enumerate(arr):
        # Check if the current number is even (divisible by 2)
        if num % 2 == 0:
            # Check if the result list is empty or if the current number is smaller than the smallest even number found so far
            if not result or num < result[0]:
                # Update the result list with the smallest even value and its index
                result = [num, i]
    
    # Return the result list containing the smallest even value and its index
    return result
``` </pre>
###### canonical_solution
<pre>     if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([4,2,3]) == [2, 1], "Error"
    assert candidate([1,2,3]) == [2, 1], "Error"
    assert candidate([]) == [], "Error"
    assert candidate([5, 0, 3, 0, 4, 2]) == [0, 1], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([1, 2, 3, 0, 5, 3]) == [0, 3], "Error"
    assert candidate([5, 4, 8, 4 ,8]) == [4, 1], "Error"
    assert candidate([7, 6, 7, 1]) == [6, 1], "Error"
    assert candidate([7, 9, 7, 1]) == [], "Error"

 </pre>
### HumanEval/121
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
 </pre>
###### answer
<pre> ```python
def solution(lst):
    # Initialize an empty list to store results
    result = []
    
    # Iterate through the list starting from index 0
    for i in range(0, len(lst), 2):
        # Check if element at current position is odd
        if lst[i] % 2 != 0:
            # Append the element to the result list
            result.append(lst[i])
            
    # Return the sum of all elements in the result list
    return sum(result)
``` </pre>
###### canonical_solution
<pre>     return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([5, 8, 7, 1])    == 12
    assert candidate([3, 3, 3, 3, 3]) == 9
    assert candidate([30, 13, 24, 321]) == 0
    assert candidate([5, 9]) == 5
    assert candidate([2, 4, 8]) == 0
    assert candidate([30, 13, 23, 32]) == 23
    assert candidate([3, 13, 2, 9]) == 3

    # Check some edge cases that are easy to work out by hand.

 </pre>
### HumanEval/74
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
 </pre>
###### answer
<pre> ```python
def total_match(lst1, lst2):
    # Calculate the total length of characters in each list
    len1 = sum(len(word) for word in lst1)
    len2 = sum(len(word) for word in lst2)
    
    # Check which list has fewer characters overall
    if len1 < len2:
        return lst1
    elif len1 > len2:
        return lst2
    else:
        # If both lists are equal in length, return the first list
        return lst1
``` </pre>
###### canonical_solution
<pre>     l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([], []) == []
    assert candidate(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    assert candidate(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert candidate(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert candidate(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert candidate(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert candidate(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']


    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([], ['this']) == []
    assert candidate(['this'], []) == []

 </pre>
### HumanEval/53
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
 </pre>
###### answer
<pre> ```python
def add(x, y):
    """Add two numbers x and y
    Args:
        x (int): first number
        y (int): second number
    Returns:
        int: Sum of x and y
    Examples:
        >>> add(2, 3)
        5
        >>> add(5, 7)
        12
    """
    return x + y
``` </pre>
###### canonical_solution
<pre>     return x + y
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    import random

    assert candidate(0, 1) == 1
    assert candidate(1, 0) == 1
    assert candidate(2, 3) == 5
    assert candidate(5, 7) == 12
    assert candidate(7, 5) == 12

    for i in range(100):
        x, y = random.randint(0, 1000), random.randint(0, 1000)
        assert candidate(x, y) == x + y

 </pre>
### HumanEval/16
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
 </pre>
###### answer
<pre> ```python
def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ignore case sensitivity when counting characters
    unique_chars = set(string.lower())
    return len(unique_chars)
``` </pre>
###### canonical_solution
<pre>     return len(set(string.lower()))
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == 0
    assert candidate('abcde') == 5
    assert candidate('abcde' + 'cade' + 'CADE') == 5
    assert candidate('aaaaAAAAaaaa') == 1
    assert candidate('Jerry jERRY JeRRRY') == 5
 </pre>
### HumanEval/58
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
 </pre>
###### answer
<pre> ```python
def common(l1, l2):
    # Find intersection of two lists using set operations
    inter = set(l1) & set(l2)
    
    # Convert back to a list and sort it
    return sorted(list(inter))
``` </pre>
###### canonical_solution
<pre>     ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []

 </pre>
### HumanEval/157
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
 </pre>
###### answer
<pre> ```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Examples:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    # Check Pythagoras theorem
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return True
    else:
        return False
``` </pre>
###### canonical_solution
<pre>     return a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(3, 4, 5) == True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1, 2, 3) == False
    assert candidate(10, 6, 8) == True
    assert candidate(2, 2, 2) == False
    assert candidate(7, 24, 25) == True
    assert candidate(10, 5, 7) == False
    assert candidate(5, 12, 13) == True
    assert candidate(15, 8, 17) == True
    assert candidate(48, 55, 73) == True

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 1, 1) == False, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(2, 2, 10) == False

 </pre>
### HumanEval/56
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
 </pre>
###### answer
<pre> ```python
def correct_bracketing(brackets: str):
    # Initialize an empty stack to keep track of unmatched opening brackets
    stack = []
    
    # Iterate through each character in the input string
    for ch in brackets:
        if ch == '<':
            # If the current character is an opening bracket, push it onto the stack
            stack.append('<')
        elif ch == '>':
            # If the current character is a closing bracket, check if the stack is not empty
            if stack:
                # Pop the last opened opening bracket from the stack
                stack.pop()
            else:
                # If the stack is empty, return False as there's no matching opening bracket
                return False
    
    # After the loop ends, check if the stack is empty. If not, there are unmatched opening brackets.
    return not stack
``` </pre>
###### canonical_solution
<pre>     depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate("<>")
    assert candidate("<<><>>")
    assert candidate("<><><<><>><>")
    assert candidate("<><><<<><><>><>><<><><<>>>")
    assert not candidate("<<<><>>>>")
    assert not candidate("><<>")
    assert not candidate("<")
    assert not candidate("<<<<")
    assert not candidate(">")
    assert not candidate("<<>")
    assert not candidate("<><><<><>><>><<>")
    assert not candidate("<><><<><>><>>><>")

 </pre>
### HumanEval/162
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
 </pre>
###### answer
<pre> ```python
def string_to_md5(text):
    import hashlib
    
    if not text:
        return None
    
    # Convert text to bytes and compute MD5 hash
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    
    return md5_hash
``` </pre>
###### canonical_solution
<pre>     import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert candidate('') == None
    assert candidate('A B C') == '0ef78513b0cb8cef12743f5aeb35f888'
    assert candidate('password') == '5f4dcc3b5aa765d61d8327deb882cf99'

    # Check some edge cases that are easy to work out by hand.
    assert True

 </pre>
### HumanEval/48
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
 </pre>
###### answer
<pre> ```python
def is_palindrome(text: str) -> bool:
    # Create a reversed copy of the input text
    reversed_text = ''.join(reversed(text))
    
    # Compare the original text with its reverse
    return text == reversed_text
``` </pre>
###### canonical_solution
<pre>     for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate('') == True
    assert candidate('aba') == True
    assert candidate('aaaaa') == True
    assert candidate('zbcd') == False
    assert candidate('xywyx') == True
    assert candidate('xywyz') == False
    assert candidate('xywzx') == False

 </pre>
