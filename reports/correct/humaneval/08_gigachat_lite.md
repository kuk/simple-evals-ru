# humaneval / gigachat-lite
### HumanEval/56
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def correct_bracketing(brackets: str):
    """ brackets is a string of "&lt;" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("&lt;")
    False
    >>> correct_bracketing("&lt;>")
    True
    >>> correct_bracketing("&lt;&lt;>&lt;>>")
    True
    >>> correct_bracketing(">&lt;&lt;>")
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
        if ch == '&lt;':
            # If the current character is an opening bracket, push it onto the stack
            stack.append('&lt;')
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
        if b == "&lt;":
            depth += 1
        else:
            depth -= 1
        if depth &lt; 0:
            return False
    return depth == 0
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate("&lt;>")
    assert candidate("&lt;&lt;>&lt;>>")
    assert candidate("&lt;>&lt;>&lt;&lt;>&lt;>>&lt;>")
    assert candidate("&lt;>&lt;>&lt;&lt;&lt;>&lt;>&lt;>>&lt;>>&lt;&lt;>&lt;>&lt;&lt;>>>")
    assert not candidate("&lt;&lt;&lt;>&lt;>>>>")
    assert not candidate(">&lt;&lt;>")
    assert not candidate("&lt;")
    assert not candidate("&lt;&lt;&lt;&lt;")
    assert not candidate(">")
    assert not candidate("&lt;&lt;>")
    assert not candidate("&lt;>&lt;>&lt;&lt;>&lt;>>&lt;>>&lt;&lt;>")
    assert not candidate("&lt;>&lt;>&lt;&lt;>&lt;>>&lt;>>>&lt;>")

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
def change_base(x: int, base: int):
    # Initialize an empty list to store converted digits
    result = []
    
    # Loop until there are no more digits left in x
    while x > 0:
        # Extract last digit of x and append it to result
        result.append(str(x % base))
        
        # Remove last digit by performing integer division
        x //= base
    
    # Reverse the list to get the digits in correct order
    return ''.join(result[::-1])
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
<pre> ```python
def triangle_area(a, h):
    """Given length of a side and height return area of a triangle.
    Args:
        a (float): Length of one side of the triangle.
        h (float): Height of the triangle.
    Returns:
        float: Area of the triangle.
    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    area = 0.5 * a * h
    return area
``` </pre>
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
### HumanEval/51
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
 </pre>
###### answer
<pre> ```python
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])
``` </pre>
###### canonical_solution
<pre>     return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate('') == ''
    assert candidate("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert candidate('fedcba') == 'fdcb'
    assert candidate('eeeee') == ''
    assert candidate('acBAA') == 'cB'
    assert candidate('EcBOO') == 'cB'
    assert candidate('ybcd') == 'ybcd'

 </pre>
### HumanEval/155
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
 </pre>
###### answer
<pre> ```python
def even_odd_count(num):
    even_count = sum(1 for digit in str(abs(num)) if int(digit) % 2 == 0)
    odd_count = len(str(abs(num))) - even_count
    return even_count, odd_count
``` </pre>
###### canonical_solution
<pre>     even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(7) == (0, 1)
    assert candidate(-78) == (1, 1)
    assert candidate(3452) == (2, 2)
    assert candidate(346211) == (3, 3)
    assert candidate(-345821) == (3, 3)
    assert candidate(-2) == (1, 0)
    assert candidate(-45347) == (2, 3)
    assert candidate(0) == (1, 0)


    # Check some edge cases that are easy to work out by hand.
    assert True

 </pre>
### HumanEval/122
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 &lt;= len(arr) &lt;= 100
        2. 1 &lt;= k &lt;= len(arr)
    """
 </pre>
###### answer
<pre> ```python
def add_elements(arr, k):
    # Initialize result variable to store the sum of elements with at most two digits
    result = 0
    
    # Iterate through the first k elements of the array
    for i in range(k):
        # Check if the current element has at most two digits
        if abs(arr[i]) &lt;= 99:
            # Add the value of the current element to the result
            result += arr[i]
            
    # Return the final result
    return result
``` </pre>
###### canonical_solution
<pre>     return sum(elem for elem in arr[:k] if len(str(elem)) &lt;= 2)
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([1,-2,-3,41,57,76,87,88,99], 3) == -4
    assert candidate([111,121,3,4000,5,6], 2) == 0
    assert candidate([11,21,3,90,5,6,7,8,9], 4) == 125
    assert candidate([111,21,3,4000,5,6,7,8,9], 4) == 24, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1], 1) == 1, "This prints if this assert fails 2 (also good for debugging!)"

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
    return ''.join(strings)
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
<pre> ```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # Check if the list is empty
        return None
    
    longest_string = strings[0]  # Initialize with the first string
    for string in strings:
        if len(string) > len(longest_string):  # Compare lengths
            longest_string = string
    
    return longest_string
``` </pre>
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
### HumanEval/78
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    """
 </pre>
###### answer
<pre> ```python
def hex_key(num):
    # Initialize count of prime hex digits
    count = 0
    
    # Iterate over each character in the hexadecimal number
    for ch in num:
        # Check if the current character is one of the prime hex digits
        if ch in {'2', '3', '5', '7', 'B', 'D'}:
            # Increment the count if it is a prime digit
            count += 1
            
    return count
``` </pre>
###### canonical_solution
<pre>     primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate("AB") == 1, "First test error: " + str(candidate("AB"))      
    assert candidate("1077E") == 2, "Second test error: " + str(candidate("1077E"))  
    assert candidate("ABED1A33") == 4, "Third test error: " + str(candidate("ABED1A33"))      
    assert candidate("2020") == 2, "Fourth test error: " + str(candidate("2020"))  
    assert candidate("123456789ABCDEF0") == 6, "Fifth test error: " + str(candidate("123456789ABCDEF0"))      
    assert candidate("112233445566778899AABBCCDDEEFF00") == 12, "Sixth test error: " + str(candidate("112233445566778899AABBCCDDEEFF00"))  


    # Check some edge cases that are easy to work out by hand.
    assert candidate([]) == 0

 </pre>
