# humaneval / gigachat-pro
### HumanEval/94
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
 </pre>
###### answer
<pre> ```python
def skjkasdkd(lst):
    # Initialize max_prime variable with the first integer in the list
    max_prime = lst[0]
    
    # Iterate through the list starting from the second element
    for num in lst[1:]:
        # Check if the current number is greater than max_prime
        if num > max_prime:
            # Check if the current number is a prime number
            if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
                # Update max_prime if the current number is both greater and prime
                max_prime = num
                
    # Return the sum of the digits of the largest prime found
    return sum(map(int, str(max_prime)))
``` </pre>
###### canonical_solution
<pre>     def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result

 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) == 10, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]) == 25, "This prints if this assert fails 2 (also good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]) == 13, "This prints if this assert fails 3 (also good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([0,724,32,71,99,32,6,0,5,91,83,0,5,6]) == 11, "This prints if this assert fails 4 (also good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate([0,81,12,3,1,21]) == 3, "This prints if this assert fails 5 (also good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([0,8,1,2,1,7]) == 7, "This prints if this assert fails 6 (also good for debugging!)"

    assert candidate([8191]) == 19, "This prints if this assert fails 7 (also good for debugging!)"
    assert candidate([8191, 123456, 127, 7]) == 19, "This prints if this assert fails 8 (also good for debugging!)"
    assert candidate([127, 97, 8192]) == 10, "This prints if this assert fails 9 (also good for debugging!)"
 </pre>
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
<pre> ```python
def anti_shuffle(s):
    # Split the input string into words
    words = s.split()
    
    # Anti-shuffle each word
    anti_shuffled_words = []
    for word in words:
        # Join individual characters of the word after arranging them in ascending order of ASCII values
        anti_shuffled_word = "".join(sorted(word, key=lambda x: ord(x)))
        anti_shuffled_words.append(anti_shuffled_word)
    
    # Reconstruct the final string with the modified words while preserving spaces
    return " ".join(anti_shuffled_words)
``` </pre>
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
<pre> ```python
def any_int(x, y, z):
    # Check if the sum of any two numbers equals the third, and all numbers are integers.
    return (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)) and \
           ((x + y == z) or (x + z == y) or (y + z == x))
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
### HumanEval/50
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
 </pre>
###### answer
<pre> ```python
def decode_shift(s: str):
    """
    Takes as input a string encoded with the `encode_shift` function. Returns the decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
``` </pre>
###### canonical_solution
<pre>     return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    from random import randint, choice
    import copy
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = encode_shift(str)
        assert candidate(copy.deepcopy(encoded_str)) == str

 </pre>
### HumanEval/49
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
 </pre>
###### answer
<pre> ```python
def modp(n: int, p: int) -> int:
    result = pow(2, n, p)
    return result
``` </pre>
###### canonical_solution
<pre>     ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate(3, 5) == 3
    assert candidate(1101, 101) == 2
    assert candidate(0, 101) == 1
    assert candidate(3, 11) == 8
    assert candidate(100, 101) == 1
    assert candidate(30, 5) == 4
    assert candidate(31, 5) == 3

 </pre>
### HumanEval/4
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
 </pre>
###### answer
<pre> ```python
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = statistics.mean(numbers)
    deviations = [abs(x - mean) for x in numbers]
    return statistics.mean(deviations)
``` </pre>
###### canonical_solution
<pre>     mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6

 </pre>
### HumanEval/116
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
 </pre>
###### answer
<pre> ```python
def sort_array(arr):
    # Create a dictionary mapping each integer to its count of ones in binary form
    ones_count = {i: bin(i).count('1') for i in arr}
    
    # Combine the integer and its count of ones into a tuple
    sorted_arr = sorted(arr, key=lambda x: (ones_count[x], x))
    
    return sorted_arr
``` </pre>
###### canonical_solution
<pre>     return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,5,2,3,4]) == [1, 2, 4, 3, 5]
    assert candidate([-2,-3,-4,-5,-6]) == [-4, -2, -6, -5, -3]
    assert candidate([1,0,2,3,4]) == [0, 1, 2, 4, 3]
    assert candidate([]) == []
    assert candidate([2,5,77,4,5,3,5,7,2,3,4]) == [2, 2, 4, 4, 3, 3, 5, 5, 5, 7, 77]
    assert candidate([3,6,44,12,32,5]) == [32, 3, 5, 6, 12, 44]
    assert candidate([2,4,8,16,32]) == [2, 4, 8, 16, 32]
    assert candidate([2,4,8,16,32]) == [2, 4, 8, 16, 32]

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

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
from math import factorial

def f(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            total = 0
            for j in range(1, i + 1):
                total += j
            result.append(total)
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
### HumanEval/158
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
 </pre>
###### answer
<pre> ```python
def find_max(words):
    def count_unique_chars(word):
        chars = set()
        for char in word:
            chars.add(char)
        return len(chars)
    
    max_unique_count = 0
    result = ''
    for word in words:
        unique_count = count_unique_chars(word)
        if unique_count > max_unique_count:
            max_unique_count = unique_count
            result = word
        elif unique_count == max_unique_count:
            if word < result:
                result = word
    return result
``` </pre>
###### canonical_solution
<pre>     return sorted(words, key = lambda x: (-len(set(x)), x))[0]
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert (candidate(["name", "of", "string"]) == "string"), "t1"
    assert (candidate(["name", "enam", "game"]) == "enam"), 't2'
    assert (candidate(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"), 't3'
    assert (candidate(["abc", "cba"]) == "abc"), 't4'
    assert (candidate(["play", "this", "game", "of","footbott"]) == "footbott"), 't5'
    assert (candidate(["we", "are", "gonna", "rock"]) == "gonna"), 't6'
    assert (candidate(["we", "are", "a", "mad", "nation"]) == "nation"), 't7'
    assert (candidate(["this", "is", "a", "prrk"]) == "this"), 't8'

    # Check some edge cases that are easy to work out by hand.
    assert (candidate(["b"]) == "b"), 't9'
    assert (candidate(["play", "play", "play"]) == "play"), 't10'

 </pre>
### HumanEval/22
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
 </pre>
###### answer
<pre> ```python
def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]
``` </pre>
###### canonical_solution
<pre>     return [x for x in values if isinstance(x, int)]
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([4, {}, [], 23.2, 9, 'adasd']) == [4, 9]
    assert candidate([3, 'c', 3, 3, 'a', 'b']) == [3, 3, 3]
 </pre>
