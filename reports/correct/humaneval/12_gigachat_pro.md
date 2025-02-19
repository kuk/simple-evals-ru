# humaneval / gigachat-pro
### HumanEval/55
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
 </pre>
###### answer
<pre> ```python
def fib(n: int):
    if n &lt;= 0:
        return None
    elif n == 1:
        return 1
    
    prev = 1
    curr = 1
    
    for _ in range(2, n):
        next_val = prev + curr
        prev = curr
        curr = next_val
        
    return curr
``` </pre>
###### canonical_solution
<pre>     if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144

 </pre>
### HumanEval/44
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
 </pre>
###### answer
<pre> ```python
def change_base(x: int, base: int) -> str:
    # Initialize an empty list to store digits in the new base
    result = []
    
    # Continue the process until the original number is reduced to zero
    while x > 0:
        # Compute the remainder when x is divided by base and append it to the result list
        result.append(x % base)
        
        # Update x to be the quotient of x divided by base
        x //= base
    
    # Since the remainder list is in reverse order, reverse it and join into a string
    return ''.join(str(digit) for digit in reversed(result))
``` </pre>
###### canonical_solution
<pre>     ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate(8, 3) == "22"
    assert candidate(9, 3) == "100"
    assert candidate(234, 2) == "11101010"
    assert candidate(16, 2) == "10000"
    assert candidate(8, 2) == "1000"
    assert candidate(7, 2) == "111"
    for x in range(2, 8):
        assert candidate(x, x + 1) == str(x)

 </pre>
### HumanEval/72
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
 </pre>
###### answer
<pre> ```python
def will_it_fly(q, w):
    # Check if the list q is balanced (palindrome)
    if q == q[::-1]:
        # Calculate the sum of elements in q
        total = sum(q)
        # Return True if the sum is less than or equal to w
        return total &lt;= w
    # If the list is not balanced, return False immediately
    return False
``` </pre>
###### canonical_solution
<pre>     if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i&lt;j:
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([3, 2, 3], 9) is True
    assert candidate([1, 2], 5) is False
    assert candidate([3], 5) is True
    assert candidate([3, 2, 3], 1) is False


    # Check some edge cases that are easy to work out by hand.
    assert candidate([1, 2, 3], 6) is False
    assert candidate([5], 5) is True

 </pre>
### HumanEval/0
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
 </pre>
###### answer
<pre> ```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list so that equal elements are рядом друг с другом
    sorted_numbers = sorted(numbers)
    
    # Iterate through the sorted list starting from the second element
    for i in range(1, len(sorted_numbers)):
        # Check the absolute difference between current and previous element
        if abs(sorted_numbers[i] - sorted_numbers[i - 1]) &lt; threshold:
            return True
            
    return False
``` </pre>
###### canonical_solution
<pre>     for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance &lt; threshold:
                    return True

    return False
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False

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
<pre> ```python
def is_prime(n):
    # Check if n is less than or equal to 1, which are not prime numbers
    if n &lt;= 1:
        return False
    
    # Check if n is 2 or 3, which are prime numbers
    if n &lt;= 3:
        return True
    
    # Ensure n is evenly divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check up to the square root of n for factors
    i = 5
    while i * i &lt;= n:
        # If n is divisible by i or i+2, it's not prime
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    # No factor was found, so n is prime
    return True
``` </pre>
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
### HumanEval/28
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
 </pre>
###### answer
<pre> ```python
def concatenate(strings: List[str]) -> str:
    return "".join(strings)
``` </pre>
###### canonical_solution
<pre>     return ''.join(strings)
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == ''
    assert candidate(['x', 'y', 'z']) == 'xyz'
    assert candidate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'
 </pre>
### HumanEval/112
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
 </pre>
###### answer
<pre> ```python
def reverse_delete(s, c):
    # Create a set from the characters of c
    chars_to_delete = set(c)
    
    # Initialize an empty list to store unique characters from s
    result = []
    
    # Iterate over each character in s
    for char in s:
        # Check if the current character is not in the set of characters to delete
        if char not in chars_to_delete:
            # Append the character to the result list
            result.append(char)
    
    # Join the list into a single string and check if it's a palindrome
    final_str = ''.join(result)
    is_palindrome = final_str == final_str[::-1]
    
    # Return the resulting string and whether it is a palindrome
    return (final_str, is_palindrome)
``` </pre>
###### canonical_solution
<pre>     s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)
 </pre>
###### test
<pre> def check(candidate):

    assert candidate("abcde","ae") == ('bcd',False)
    assert candidate("abcdef", "b") == ('acdef',False)
    assert candidate("abcdedcba","ab") == ('cdedc',True)
    assert candidate("dwik","w") == ('dik',False)
    assert candidate("a","a") == ('',True)
    assert candidate("abcdedcba","") == ('abcdedcba',True)
    assert candidate("abcdedcba","v") == ('abcdedcba',True)
    assert candidate("vabba","v") == ('abba',True)
    assert candidate("mamma", "mia") == ("", True)
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
    # Convert the string to lowercase to ignore case differences
    distinct_chars = set(string.lower())
    return len(distinct_chars)
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
### HumanEval/85
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
 </pre>
###### answer
<pre> ```python
def add(lst):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each element in the input list
    for i in range(len(lst)):
        # Check if the current index is odd and the element is even
        if i % 2 != 0 and lst[i] % 2 == 0:
            # Append the element to the result list
            result.append(lst[i])
            
    # Return the sum of all elements in the result list
    return sum(result)
``` </pre>
###### canonical_solution
<pre>     return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([4, 88]) == 88
    assert candidate([4, 5, 6, 7, 2, 122]) == 122
    assert candidate([4, 0, 6, 7]) == 0
    assert candidate([4, 4, 6, 8]) == 12

    # Check some edge cases that are easy to work out by hand.
    
 </pre>
### HumanEval/7
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
 </pre>
###### answer
<pre> ```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
``` </pre>
###### canonical_solution
<pre>     return [x for x in strings if substring in x]
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
    assert candidate(['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx') == ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']
    assert candidate(['grunt', 'trumpet', 'prune', 'gruesome'], 'run') == ['grunt', 'prune']
 </pre>
