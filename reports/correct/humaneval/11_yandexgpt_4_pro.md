# humaneval / yandexgpt-4-pro
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
<pre> ```
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
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
### HumanEval/8
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
 </pre>
###### answer
<pre> ```
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1

    sum_ = 0
    product = 1
    for num in numbers:
        sum_ += num
        product *= num

    return sum_, product
``` </pre>
###### canonical_solution
<pre>     sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == (0, 1)
    assert candidate([1, 1, 1]) == (3, 1)
    assert candidate([100, 0]) == (100, 0)
    assert candidate([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7)
    assert candidate([10]) == (10, 10)
 </pre>
### HumanEval/15
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
 </pre>
###### answer
<pre> ```
def string_sequence(n: int) -> str:
    result = ''

    for i in range(n + 1):
        result += str(i) + ' '

    return result.strip()
``` </pre>
###### canonical_solution
<pre>     return ' '.join([str(x) for x in range(n + 1)])
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'
 </pre>
### HumanEval/36
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
 </pre>
###### answer
<pre> ```
def fizz_buzz(n: int):
    count = 0

    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            if '7' in str(i):
                count += str(i).count('7')

    return count
``` </pre>
###### canonical_solution
<pre>     ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate(50) == 0
    assert candidate(78) == 2
    assert candidate(79) == 3
    assert candidate(100) == 3
    assert candidate(200) == 6
    assert candidate(4000) == 192
    assert candidate(10000) == 639
    assert candidate(100000) == 8026

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
<pre> ```
def add(x: int, y: int):
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
<pre> ```
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    result = []

    for string in strings:
        if string.startswith(prefix):
            result.append(string)

    return result
``` </pre>
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
### HumanEval/5
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
 </pre>
###### answer
<pre> ```
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []

    if not numbers:
        return numbers

    for i in range(len(numbers)):
        if i == 0:
            result.append(numbers[0])
        else:
            result.append(delimeter)
            result.append(numbers[i])

    return result
``` </pre>
###### canonical_solution
<pre>     if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 7) == []
    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]
 </pre>
### HumanEval/107
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 &lt;= n &lt;= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
 </pre>
###### answer
<pre> ```
def even_odd_palindrome(n):
    # Create two counters, one for even palindromes and one for odd palindromes
    even_count = 0
    odd_count = 0

    # Iterate through numbers from 1 to n
    for i in range(1, n + 1):
        # Check if the number is a palindrome
        if str(i) == str(i)[::-1]:
            # If the number is even, increment the even count
            if i % 2 == 0:
                even_count += 1
            else:  # If the number is odd, increment the odd count
                odd_count += 1

    return (even_count, odd_count)
``` </pre>
###### canonical_solution
<pre>     def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n+1):
        if i%2 == 1 and is_palindrome(i):
                odd_palindrome_count += 1
        elif i%2 == 0 and is_palindrome(i):
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(123) == (8, 13)
    assert candidate(12) == (4, 6)
    assert candidate(3) == (1, 2)
    assert candidate(63) == (6, 8)
    assert candidate(25) == (5, 6)
    assert candidate(19) == (4, 6)
    assert candidate(9) == (4, 5), "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == (0, 1), "This prints if this assert fails 2 (also good for debugging!)"

 </pre>
### HumanEval/117
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
 </pre>
###### answer
<pre> ```
def select_words(s, n):
    # Create an empty list to store the words that contain exactly n consonants
    result = []

    # Split the string into words
    words = s.split()

    # Loop through each word in the string
    for word in words:
        # Count the number of consonants in the word
        count = 0
        for char in word:
            if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
                count += 1
        if count == n:
            # If the word contains exactly n consonants, add it to the result list
            result.append(word)

    return result
``` </pre>
###### canonical_solution
<pre>     result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result

 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate("Mary had a little lamb", 4) == ["little"], "First test error: " + str(candidate("Mary had a little lamb", 4))      
    assert candidate("Mary had a little lamb", 3) == ["Mary", "lamb"], "Second test error: " + str(candidate("Mary had a little lamb", 3))  
    assert candidate("simple white space", 2) == [], "Third test error: " + str(candidate("simple white space", 2))      
    assert candidate("Hello world", 4) == ["world"], "Fourth test error: " + str(candidate("Hello world", 4))  
    assert candidate("Uncle sam", 3) == ["Uncle"], "Fifth test error: " + str(candidate("Uncle sam", 3))


    # Check some edge cases that are easy to work out by hand.
    assert candidate("", 4) == [], "1st edge test error: " + str(candidate("", 4))
    assert candidate("a b c d e f", 1) == ["b", "c", "d", "f"], "2nd edge test error: " + str(candidate("a b c d e f", 1))

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
<pre> ```
def common(l1: list, l2: list):
    # Create a set to store unique elements from both lists
    common_elements = set()

    # Iterate through each list
    for num in l1:
        if num in l2 and num not in common_elements:
            common_elements.add(num)

    return sorted(common_elements)
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
