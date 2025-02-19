# humaneval / gigachat-max
### HumanEval/39
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
 </pre>
###### answer
<pre> ```python
from math import gcd

def is_prime(n: int) -> bool:
    if n &lt;= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i &lt;= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n: int) -> int:
    fib_sequence = [0, 1]
    index = 0
    count = 0
    
    while count &lt; n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        
        if is_prime(next_fib):
            count += 1
            index = len(fib_sequence) - 1
            
    return fib_sequence[index]
``` </pre>
###### canonical_solution
<pre>     import math

    def is_prime(p):
        if p &lt; 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate(1) == 2
    assert candidate(2) == 3
    assert candidate(3) == 5
    assert candidate(4) == 13
    assert candidate(5) == 89
    assert candidate(6) == 233
    assert candidate(7) == 1597
    assert candidate(8) == 28657
    assert candidate(9) == 514229
    assert candidate(10) == 433494437

 </pre>
### HumanEval/124
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
 </pre>
###### answer
<pre> ```python
import re

def valid_date(date):
    # Check if the date string is empty
    if not date:
        return False
    
    # Check if the date is in the correct format (mm-dd-yyyy)
    pattern = r'^\d{2}-\d{2}-\d{4}$'
    if not re.match(pattern, date):
        return False
    
    # Extract day, month, and year from the date string
    parts = date.split('-')
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])
    
    # Validate the month
    if month &lt; 1 or month > 12:
        return False
    
    # Validate the day based on the month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        max_days = 31
    elif month == 2:
        max_days = 29
    else:
        max_days = 30
    
    if day &lt; 1 or day > max_days:
        return False
    
    # If we reach here, the date is valid
    return True
``` </pre>
###### canonical_solution
<pre>     try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month &lt; 1 or month > 12:
            return False
        if month in [1,3,5,7,8,10,12] and day &lt; 1 or day > 31:
            return False
        if month in [4,6,9,11] and day &lt; 1 or day > 30:
            return False
        if month == 2 and day &lt; 1 or day > 29:
            return False
    except:
        return False

    return True
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate('03-11-2000') == True

    assert candidate('15-01-2012') == False

    assert candidate('04-0-2040') == False

    assert candidate('06-04-2020') == True

    assert candidate('01-01-2007') == True

    assert candidate('03-32-2011') == False

    assert candidate('') == False

    assert candidate('04-31-3000') == False

    assert candidate('06-06-2005') == True

    assert candidate('21-31-2000') == False

    assert candidate('04-12-2003') == True

    assert candidate('04122003') == False

    assert candidate('20030412') == False

    assert candidate('2003-04') == False

    assert candidate('2003-04-12') == False

    assert candidate('04-2003') == False
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
    # Check for edge cases where n &lt;= 1
    if n &lt;= 1:
        return False
    
    # Check for even numbers greater than 2
    if n > 2 and n % 2 == 0:
        return False
    
    # Check for odd divisors from 3 to sqrt(n)
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    
    # If no divisor found, it's prime
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
### HumanEval/89
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
 </pre>
###### answer
<pre> ```python
def encrypt(s):
    encrypted = ""
    for char in s:
        # Get ASCII value of character
        ascii_value = ord(char)
        
        # Shift the character by 2 * 2 positions (4 positions) in the alphabet
        shifted_ascii_value = ascii_value + 4
        
        # Ensure we wrap around if necessary (e.g., 'z' becomes 'd')
        if shifted_ascii_value > ord('z'):
            wrapped_ascii_value = shifted_ascii_value - 26
        else:
            wrapped_ascii_value = shifted_ascii_value
            
        # Convert back to character and append to result
        encrypted += chr(wrapped_ascii_value)
    
    return encrypted
```

This implementation follows the given rules exactly: it shifts each letter in the input string by 4 positions in the alphabet, wrapping around from 'z' to 'a' when necessary. </pre>
###### canonical_solution
<pre>     d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate('hi') == 'lm', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('asdfghjkl') == 'ewhjklnop', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('gf') == 'kj', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('et') == 'ix', "This prints if this assert fails 1 (good for debugging!)"

    assert candidate('faewfawefaewg')=='jeiajeaijeiak', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('hellomyfriend')=='lippsqcjvmirh', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh')=='hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl', "This prints if this assert fails 3 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate('a')=='e', "This prints if this assert fails 2 (also good for debugging!)"

 </pre>
### HumanEval/152
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
 </pre>
###### answer
<pre> ```python
def compare(game, guess):
    return [abs(g - s) for g, s in zip(guess, game)]
``` </pre>
###### canonical_solution
<pre>     return [abs(x-y) for x,y in zip(game,guess)]
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([1,2,3,4,5,1],[1,2,3,4,2,-2])==[0,0,0,0,3,3], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([0,0,0,0,0,0],[0,0,0,0,0,0])==[0,0,0,0,0,0], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,2,3],[-1,-2,-3])==[2,4,6], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,2,3,5],[-1,2,3,4])==[2,0,0,1], "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

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
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list to facilitate pairwise comparison
    sorted_numbers = sorted(numbers)
    
    # Iterate through adjacent pairs to check if their difference is less than the threshold
    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i + 1] - sorted_numbers[i]) &lt; threshold:
            return True
    
    # If no such pair exists, return False
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
from collections import Counter

def find_max(words):
    max_unique_chars = 0
    result = ""
    
    for word in words:
        # Count unique characters in each word
        unique_char_count = len(set(word))
        
        if (unique_char_count > max_unique_chars) or \
           (unique_char_count == max_unique_chars and word &lt; result):
            max_unique_chars = unique_char_count
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
    return text == text[::-1]
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
### HumanEval/104
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
 </pre>
###### answer
<pre> ```python
def unique_digits(x):
    def has_even_digit(n):
        while n > 0:
            if (n % 10) % 2 == 0:
                return True
            n //= 10
        return False

    result = [num for num in x if not has_even_digit(num)]
    return sorted(result)
``` </pre>
###### canonical_solution
<pre>     odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

    # Check some edge cases that are easy to work out by hand.
    assert True

 </pre>
