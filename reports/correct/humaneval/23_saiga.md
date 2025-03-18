# humaneval / saiga-nemo
### HumanEval/86
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
 </pre>
###### answer
<pre> def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    return ' '.join(''.join(sorted(word)) for word in s.split())

# Example usage
print(anti_shuffle('Hi'))  # Output: 'Hi'
print(anti_shuffle('hello'))  # Output: 'ehllo'
print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor' </pre>
###### canonical_solution
<pre>     return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate('Hi') == 'Hi'
    assert candidate('hello') == 'ehllo'
    assert candidate('number') == 'bemnru'
    assert candidate('abcd') == 'abcd'
    assert candidate('Hello World!!!') == 'Hello !!!Wdlor'
    assert candidate('') == ''
    assert candidate('Hi. My name is Mister Robot. How are you?') == '.Hi My aemn is Meirst .Rboot How aer ?ouy'
    # Check some edge cases that are easy to work out by hand.
    assert True

 </pre>
### HumanEval/92
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
 </pre>
###### answer
<pre> def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns True if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns False in any other cases.

    Parameters:
    x (int): The first number
    y (int): The second number
    z (int): The third number

    Returns:
    bool: True if one of the numbers is equal to the sum of the other two and all are integers, False otherwise
    """
    # Check if all inputs are integers
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False

    # Check if any number is equal to the sum of the other two
    return x == y + z or y == x + z or z == x + y

# Test cases
print(any_int(5, 2, 7))  # ➞ True
print(any_int(3, 2, 2))  # ➞ False
print(any_int(3, -2, 1))  # ➞ True
print(any_int(3.6, -2.2, 2))  # ➞ False </pre>
###### canonical_solution
<pre>     
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(2, 3, 1)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(2.5, 2, 3)==False, "This prints if this assert fails 2 (good for debugging!)"
    assert candidate(1.5, 5, 3.5)==False, "This prints if this assert fails 3 (good for debugging!)"
    assert candidate(2, 6, 2)==False, "This prints if this assert fails 4 (good for debugging!)"
    assert candidate(4, 2, 2)==True, "This prints if this assert fails 5 (good for debugging!)"
    assert candidate(2.2, 2.2, 2.2)==False, "This prints if this assert fails 6 (good for debugging!)"
    assert candidate(-4, 6, 2)==True, "This prints if this assert fails 7 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(2,1,1)==True, "This prints if this assert fails 8 (also good for debugging!)"
    assert candidate(3,4,7)==True, "This prints if this assert fails 9 (also good for debugging!)"
    assert candidate(3.0,4,7)==False, "This prints if this assert fails 10 (also good for debugging!)"

 </pre>
### HumanEval/6
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
 </pre>
###### answer
<pre> def parse_nested_parens(paren_string: str) -> List[int]:
    def count_nesting(parens: str) -> int:
        count = 0
        max_count = 0
        for char in parens:
            if char == '(':
                count += 1
                max_count = max(max_count, count)
            elif char == ')':
                count -= 1
        return max_count

    # Split the input string by spaces to get individual groups
    groups = paren_string.split()
    # Apply the count_nesting function to each group
    return [count_nesting(group) for group in groups]

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3] </pre>
###### canonical_solution
<pre>     def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]
 </pre>
### HumanEval/57
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
 </pre>
###### answer
<pre> def monotonic(l: list) -> bool:
    if not l:
        return True  # Empty list is considered monotonically increasing or decreasing

    # Check if the list is monotonically increasing
    if all(l[i] &lt;= l[i + 1] for i in range(len(l) - 1)):
        return True

    # Check if the list is monotonically decreasing
    if all(l[i] >= l[i + 1] for i in range(len(l) - 1)):
        return True

    return False </pre>
###### canonical_solution
<pre>     if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10]) == True
    assert candidate([1, 2, 4, 20]) == True
    assert candidate([1, 20, 4, 10]) == False
    assert candidate([4, 1, 0, -10]) == True
    assert candidate([4, 1, 1, 0]) == True
    assert candidate([1, 2, 3, 2, 5, 60]) == False
    assert candidate([1, 2, 3, 4, 5, 60]) == True
    assert candidate([9, 9, 9, 9]) == True

 </pre>
### HumanEval/76
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
 </pre>
###### answer
<pre> def is_simple_power(x, n):
    """
    Returns True if a number x is a simple power of n, and False otherwise.
    A number x is a simple power of n if n**int = x for some integer int.

    Parameters:
    x (int): The number to check.
    n (int): The base number.

    Returns:
    bool: True if x is a simple power of n, False otherwise.
    """
    if n == 1:
        return x == 1
    else:
        return x == n ** int(math.log(x, n))

# Example usage
import math

print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(3, 1))  # False
print(is_simple_power(5, 3))  # False </pre>
###### canonical_solution
<pre>     if (n == 1): 
        return (x == 1) 
    power = 1
    while (power &lt; x): 
        power = power * n 
    return (power == x) 
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(16, 2)== True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(143214, 16)== False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(4, 2)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(9, 3)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(16, 4)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(24, 2)==False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(128, 4)==False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(12, 6)==False, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 1)==True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(1, 12)==True, "This prints if this assert fails 2 (also good for debugging!)"

 </pre>
### HumanEval/29
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
 </pre>
###### answer
<pre> def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Parameters:
    - strings (List[str]): The list of strings to filter.
    - prefix (str): The prefix to match at the beginning of each string.

    Returns:
    - List[str]: A new list containing only the strings that start with the given prefix.
    """
    return [s for s in strings if s.startswith(prefix)] </pre>
###### canonical_solution
<pre>     return [x for x in strings if x.startswith(prefix)]
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 'john') == []
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']
 </pre>
### HumanEval/30
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
 </pre>
###### answer
<pre> def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
    return [num for num in l if num > 0] </pre>
###### canonical_solution
<pre>     return [e for e in l if e > 0]
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate([-1, -2, 4, 5, 6]) == [4, 5, 6]
    assert candidate([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 3, 9, 123, 1]
    assert candidate([-1, -2]) == []
    assert candidate([]) == []

 </pre>
### HumanEval/45
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
 </pre>
###### answer
<pre> def triangle_area(a, h):
    """
    Given length of a side and height, return area for a triangle.

    Parameters:
    a (float): The length of a side of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    # Area of a triangle is calculated as 0.5 * base * height
    return 0.5 * a * h

# Example usage
print(triangle_area(5, 3))  # Output: 7.5 </pre>
###### canonical_solution
<pre>     return a * h / 2.0
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0

 </pre>
### HumanEval/12
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
 </pre>
###### answer
<pre> from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. If there are multiple strings of the same
    length, return the first one. If the input list is empty, return None.

    Parameters:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string or None if the list is empty.
    """
    if not strings:
        return None

    longest_str = strings[0]
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string

    return longest_str

# Example usage
print(longest([]))  # Output: None
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc' </pre>
###### canonical_solution
<pre>     if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == None
    assert candidate(['x', 'y', 'z']) == 'x'
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'
 </pre>
### HumanEval/31
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
 </pre>
###### answer
<pre> def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n &lt;= 1:
        return False
    elif n &lt;= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i &lt;= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True </pre>
###### canonical_solution
<pre>     if n &lt; 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate(6) == False
    assert candidate(101) == True
    assert candidate(11) == True
    assert candidate(13441) == True
    assert candidate(61) == True
    assert candidate(4) == False
    assert candidate(1) == False
    assert candidate(5) == True
    assert candidate(11) == True
    assert candidate(17) == True
    assert candidate(5 * 17) == False
    assert candidate(11 * 7) == False
    assert candidate(13441 * 19) == False

 </pre>
