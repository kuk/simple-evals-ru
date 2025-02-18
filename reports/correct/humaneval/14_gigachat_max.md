# humaneval / gigachat-max
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
import hashlib

def string_to_md5(text):
    if not text:
        return None
    
    # Encode the input string to bytes (utf-8)
    byte_text = text.encode("utf-8")
    
    # Create an MD5 hash object
    md5_hash = hashlib.md5(byte_text)
    
    # Return the hexadecimal digest of the hash
    return md5_hash.hexdigest()
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
### HumanEval/20
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
 </pre>
###### answer
<pre> ```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Initialize variables to track the smallest difference and the corresponding pair
    min_diff = float('inf')
    result = (numbers[0], numbers[1])
    
    # Iterate through all pairs of elements
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            
            if diff < min_diff:
                min_diff = diff
                result = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
                
    return result
``` </pre>
###### canonical_solution
<pre>     closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1]) == (2.2, 3.1)

 </pre>
### HumanEval/139
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
 </pre>
###### answer
<pre> ```python
import math

def special_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result
``` </pre>
###### canonical_solution
<pre>     fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(4) == 288, "Test 4"
    assert candidate(5) == 34560, "Test 5"
    assert candidate(7) == 125411328000, "Test 7"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == 1, "Test 1"

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
<pre> ```python
def any_int(x, y, z):
    # Check if all arguments are integers
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    
    # Check if one number is the sum of the other two
    return x + y == z or x + z == y or y + z == x
``` </pre>
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
### HumanEval/106
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
 </pre>
###### answer
<pre> ```python
def f(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            # Calculate factorial of i
            factorial = 1
            for j in range(2, i + 1):
                factorial *= j
            result.append(factorial)
        else:
            # Calculate sum of numbers from 1 to i
            total_sum = sum(range(1, i + 1))
            result.append(total_sum)
    return result
``` </pre>
###### canonical_solution
<pre>     ret = []
    for i in range(1,n+1):
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret
 </pre>
###### test
<pre> def check(candidate):

    assert candidate(5) == [1, 2, 6, 24, 15]
    assert candidate(7) == [1, 2, 6, 24, 15, 720, 28]
    assert candidate(1) == [1]
    assert candidate(3) == [1, 2, 6]
 </pre>
### HumanEval/59
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
 </pre>
###### answer
<pre> ```python
def largest_prime_factor(n: int) -> int:
    # Start from the smallest possible prime number (2).
    i = 2
    
    # Keep dividing by i until it no longer divides evenly.
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            # Move to the next potential divisor.
            i += 1
    
    # If n is still greater than 1 at this point, then it's the largest prime factor.
    return max(i, n)
``` </pre>
###### canonical_solution
<pre>     def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29

 </pre>
### HumanEval/40
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
 </pre>
###### answer
<pre> ```python
def triples_sum_to_zero(l: list) -> bool:
    # Sort the list to facilitate two-pointer approach
    l.sort()
    
    n = len(l)
    
    # Iterate through each element in the sorted list
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            total = l[i] + l[left] + l[right]
            
            if total == 0:
                return True
            elif total < 0:
                left += 1
            else:
                right -= 1
                
    # If no such triplets found, return False
    return False
``` </pre>
###### canonical_solution
<pre>     for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate([1, 3, 5, 0]) == False
    assert candidate([1, 3, 5, -1]) == False
    assert candidate([1, 3, -2, 1]) == True
    assert candidate([1, 2, 3, 7]) == False
    assert candidate([1, 2, 5, 7]) == False
    assert candidate([2, 4, -5, 3, 9, 7]) == True
    assert candidate([1]) == False
    assert candidate([1, 3, 5, -100]) == False
    assert candidate([100, 3, 5, -100]) == False

 </pre>
### HumanEval/13
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
 </pre>
###### answer
<pre> ```python
def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)
``` </pre>
###### canonical_solution
<pre>     while b:
        a, b = b, a % b
    return a
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3, 7) == 1
    assert candidate(10, 15) == 5
    assert candidate(49, 14) == 7
    assert candidate(144, 60) == 12
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
    # Remove all characters from 's' that appear in 'c'
    filtered_s = ''.join([char for char in s if char not in c])
    
    # Check if the resulting string is a palindrome
    reversed_filtered_s = filtered_s[::-1]
    is_palindrome = (filtered_s == reversed_filtered_s)
    
    # Return the result string and whether it's a palindrome
    return (filtered_s, is_palindrome)
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
