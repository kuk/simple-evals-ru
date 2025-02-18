# humaneval / gigachat-lite
### HumanEval/82
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
 </pre>
###### answer
<pre> ```python
def prime_length(string):
    # Check if the length of the string is greater than 1 (since 0 and 1 are not primes)
    if len(string) > 1:
        # Check if the length is divisible by any number other than 1 and itself
        return all(string[:i] != string[i:] for i in range(2, len(string)))
    else:
        # Return False if the string length is less than or equal to 1
        return False
``` </pre>
###### canonical_solution
<pre>     l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate('Hello') == True
    assert candidate('abcdcba') == True
    assert candidate('kittens') == True
    assert candidate('orange') == False
    assert candidate('wow') == True
    assert candidate('world') == True
    assert candidate('MadaM') == True
    assert candidate('Wow') == True
    assert candidate('') == False
    assert candidate('HI') == True
    assert candidate('go') == True
    assert candidate('gogo') == False
    assert candidate('aaaaaaaaaaaaaaa') == False

    # Check some edge cases that are easy to work out by hand.
    assert candidate('Madam') == True
    assert candidate('M') == False
    assert candidate('0') == False

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 49
     44     assert candidate('M') == False
     45     assert candidate('0') == False
---> 49 check(prime_length)
Cell In[1], line 31, in check(candidate)
     29 assert candidate('abcdcba') == True
     30 assert candidate('kittens') == True
---> 31 assert candidate('orange') == False
     32 assert candidate('wow') == True
     33 assert candidate('world') == True
AssertionError:  </pre>
### HumanEval/110
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
 </pre>
###### answer
<pre> ```python
def exchange(lst1, lst2):
    # Check if both lists are empty or not
    if not lst1 or not lst2:
        return "NO"
    
    # Iterate through lst1 and check each element
    for num in lst1:
        # Check if the current element is even
        if num % 2 == 0:
            continue
        
        # Find the corresponding index in lst2 where the element can be swapped
        idx = next((i for i, x in enumerate(lst2) if x == num), None)
        
        # If there's no such element in lst2, return 'NO'
        if idx is None:
            return "NO"
        
        # Swap the found element with the first even element in lst1
        lst1[lst1.index(num)] = lst1[0]
        lst1[0] = num
        break
    
    # Return "YES" if lst1 contains only even numbers after swap
    return "YES" if all(x % 2 == 0 for x in lst1) else "NO"
``` </pre>
###### canonical_solution
<pre>     odd = 0
    even = 0
    for i in lst1:
        if i%2 == 1:
            odd += 1
    for i in lst2:
        if i%2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"
            
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert candidate([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert candidate([1, 2, 3, 4], [2, 1, 4, 3]) == "YES" 
    assert candidate([5, 7, 3], [2, 6, 4]) == "YES"
    assert candidate([5, 7, 3], [2, 6, 3]) == "NO" 
    assert candidate([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1]) == "NO"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([100, 200], [200, 200]) == "YES"

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 61
     56     # Check some edge cases that are easy to work out by hand.
     57     assert candidate([100, 200], [200, 200]) == "YES"
---> 61 check(exchange)
Cell In[1], line 49, in check(candidate)
     46 def check(candidate):
     47 
     48     # Check some simple cases
---> 49     assert candidate([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
     50     assert candidate([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
     51     assert candidate([1, 2, 3, 4], [2, 1, 4, 3]) == "YES" 
AssertionError:  </pre>
### HumanEval/95
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
 </pre>
###### answer
<pre> ```python
def check_dict_case(dict):
    # Check if dict is empty
    if not dict:
        return False
    
    # Initialize counters for lower and upper case keys
    lower_count = 0
    upper_count = 0
    
    # Iterate over each key-value pair in the dictionary
    for key in dict:
        # Convert key to lowercase and increment counter
        if key.islower():
            lower_count += 1
        
        # Convert key to uppercase and increment counter
        elif key.isupper():
            upper_count += 1
        
        # If both cases are true, return False
        elif key.isalpha() and (key.islower() or key.isupper()):
            return False
    
    # Return True if either count equals len(dict)
    return lower_count == len(dict) or upper_count == len(dict)
``` </pre>
###### canonical_solution
<pre>     if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():

            if isinstance(key, str) == False:
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                    state = "mixed"
                    break
            else:
                break
        return state == "upper" or state == "lower" 
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate({"p":"pineapple", "b":"banana"}) == True, "First test error: " + str(candidate({"p":"pineapple", "b":"banana"}))
    assert candidate({"p":"pineapple", "A":"banana", "B":"banana"}) == False, "Second test error: " + str(candidate({"p":"pineapple", "A":"banana", "B":"banana"}))
    assert candidate({"p":"pineapple", 5:"banana", "a":"apple"}) == False, "Third test error: " + str(candidate({"p":"pineapple", 5:"banana", "a":"apple"}))
    assert candidate({"Name":"John", "Age":"36", "City":"Houston"}) == False, "Fourth test error: " + str(candidate({"Name":"John", "Age":"36", "City":"Houston"}))
    assert candidate({"STATE":"NC", "ZIP":"12345" }) == True, "Fifth test error: " + str(candidate({"STATE":"NC", "ZIP":"12345" }))      
    assert candidate({"fruit":"Orange", "taste":"Sweet" }) == True, "Fourth test error: " + str(candidate({"fruit":"Orange", "taste":"Sweet" }))      


    # Check some edge cases that are easy to work out by hand.
    assert candidate({}) == False, "1st edge test error: " + str(candidate({}))

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AttributeError                            Traceback (most recent call last)Cell In[1], line 61
     56     # Check some edge cases that are easy to work out by hand.
     57     assert candidate({}) == False, "1st edge test error: " + str(candidate({}))
---> 61 check(check_dict_case)
Cell In[1], line 50, in check(candidate)
     48 assert candidate({"p":"pineapple", "b":"banana"}) == True, "First test error: " + str(candidate({"p":"pineapple", "b":"banana"}))
     49 assert candidate({"p":"pineapple", "A":"banana", "B":"banana"}) == False, "Second test error: " + str(candidate({"p":"pineapple", "A":"banana", "B":"banana"}))
---> 50 assert candidate({"p":"pineapple", 5:"banana", "a":"apple"}) == False, "Third test error: " + str(candidate({"p":"pineapple", 5:"banana", "a":"apple"}))
     51 assert candidate({"Name":"John", "Age":"36", "City":"Houston"}) == False, "Fourth test error: " + str(candidate({"Name":"John", "Age":"36", "City":"Houston"}))
     52 assert candidate({"STATE":"NC", "ZIP":"12345" }) == True, "Fifth test error: " + str(candidate({"STATE":"NC", "ZIP":"12345" }))      
Cell In[1], line 30, in check_dict_case(dict)
     27 # Iterate over each key-value pair in the dictionary
     28 for key in dict:
     29     # Convert key to lowercase and increment counter
---> 30     if key.islower():
     31         lower_count += 1
     33     # Convert key to uppercase and increment counter
AttributeError: 'int' object has no attribute 'islower' </pre>
### HumanEval/38
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
 </pre>
###### answer
<pre> ```python
def decode_cyclic(s: str):
    """
    Takes as input a string encoded with `encode_cyclic` function and returns the original unencoded string.
    """
    # Split the string into groups of 3 characters
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    
    # Join the groups back together without any cyclic encoding
    return ''.join(groups)
``` </pre>
###### canonical_solution
<pre>     return encode_cyclic(encode_cyclic(s))
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    from random import randint, choice
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = encode_cyclic(str)
        assert candidate(encoded_str) == str

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 50
     45         encoded_str = encode_cyclic(str)
     46         assert candidate(encoded_str) == str
---> 50 check(decode_cyclic)
Cell In[1], line 46, in check(candidate)
     44 str = ''.join(choice(letters) for i in range(randint(10, 20)))
     45 encoded_str = encode_cyclic(str)
---> 46 assert candidate(encoded_str) == str
AssertionError:  </pre>
### HumanEval/134
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 </pre>
###### answer
<pre> ```python
def check_if_last_char_is_a_letter(txt):
    # Check if the text is empty
    if not txt:
        return False
    
    # Get the last character of the text
    last_char = txt[-1]
    
    # Check if the last character is alphabetic (upper or lower case)
    if 'a' <= last_char <= 'z' or 'A' <= last_char <= 'Z':
        # Check if it's not followed by a space
        if txt.rfind(' ') == -1 or txt.rfind(' ') < len(txt) - 2:
            return True
    
    return False
``` </pre>
###### canonical_solution
<pre>  
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate("apple") == False
    assert candidate("apple pi e") == True
    assert candidate("eeeee") == False
    assert candidate("A") == True
    assert candidate("Pumpkin pie ") == False
    assert candidate("Pumpkin pie 1") == False
    assert candidate("") == False
    assert candidate("eeeee e ") == False
    assert candidate("apple pie") == False
    assert candidate("apple pi e ") == False

    # Check some edge cases that are easy to work out by hand.
    assert True

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 55
     50     # Check some edge cases that are easy to work out by hand.
     51     assert True
---> 55 check(check_if_last_char_is_a_letter)
Cell In[1], line 39, in check(candidate)
     36 def check(candidate):
     37 
     38     # Check some simple cases
---> 39     assert candidate("apple") == False
     40     assert candidate("apple pi e") == True
     41     assert candidate("eeeee") == False
AssertionError:  </pre>
### HumanEval/19
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
 </pre>
###### answer
<pre> ```python
def sort_numbers(numbers: str) -> str:
    # Convert input string into a list of characters
    chars = list(numbers)
    
    # Sort the characters in ascending order (smallest to largest)
    chars.sort()
    
    # Join the sorted characters back into a single string
    return ''.join(chars)
``` </pre>
###### canonical_solution
<pre>     value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('three') == 'three'
    assert candidate('three five nine') == 'three five nine'
    assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
    assert candidate('six five four three two one zero') == 'zero one two three four five six'
 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 42
     38     assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
     39     assert candidate('six five four three two one zero') == 'zero one two three four five six'
---> 42 check(sort_numbers)
Cell In[1], line 36, in check(candidate)
     34 def check(candidate):
     35     assert candidate('') == ''
---> 36     assert candidate('three') == 'three'
     37     assert candidate('three five nine') == 'three five nine'
     38     assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
AssertionError:  </pre>
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
    """Find the word with maximum number of unique characters in a list of strings.
    
    Arguments:
        words {list} -- A list of strings.
    
    Returns:
        str -- The word with the most unique characters.
    """
    # Initialize variables to store the maximum number of unique characters and its corresponding word
    max_unique_chars = 0
    max_word = None
    
    # Iterate over each word in the list
    for word in words:
        # Count the number of unique characters in the current word
        unique_char_count = len(set(word))
        
        # Check if the current word has more unique characters than the previously found maximum
        if unique_char_count > max_unique_chars:
            # Update the maximum number of unique characters and the corresponding word
            max_unique_chars = unique_char_count
            max_word = word
    
    # Return the word with the most unique characters
    return max_word
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
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 62
     57     assert (candidate(["b"]) == "b"), 't9'
     58     assert (candidate(["play", "play", "play"]) == "play"), 't10'
---> 62 check(find_max)
Cell In[1], line 48, in check(candidate)
     44 def check(candidate):
     45 
     46     # Check some simple cases
     47     assert (candidate(["name", "of", "string"]) == "string"), "t1"
---> 48     assert (candidate(["name", "enam", "game"]) == "enam"), 't2'
     49     assert (candidate(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"), 't3'
     50     assert (candidate(["abc", "cba"]) == "abc"), 't4'
AssertionError: t2 </pre>
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
    # Create an empty list to store the encrypted characters
    encrypted_chars = []
    
    # Iterate over each character in the input string
    for ch in s:
        # Get ASCII value of the current character
        ascii_value = ord(ch)
        
        # Rotate the ASCII value by 2 * 2 (48 modulo 26) positions
        new_ascii_value = (ascii_value + 48) % 26
        
        # Convert back to a character and append it to the list
        encrypted_chars.append(chr(new_ascii_value))
    
    # Join the list into a single string and return the result
    return ''.join(encrypted_chars)
``` </pre>
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
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 53
     48     # Check some edge cases that are easy to work out by hand.
     49     assert candidate('a')=='e', "This prints if this assert fails 2 (also good for debugging!)"
---> 53 check(encrypt)
Cell In[1], line 39, in check(candidate)
     36 def check(candidate):
     37 
     38     # Check some simple cases
---> 39     assert candidate('hi') == 'lm', "This prints if this assert fails 1 (good for debugging!)"
     40     assert candidate('asdfghjkl') == 'ewhjklnop', "This prints if this assert fails 1 (good for debugging!)"
     41     assert candidate('gf') == 'kj', "This prints if this assert fails 1 (good for debugging!)"
AssertionError: This prints if this assert fails 1 (good for debugging!) </pre>
### HumanEval/138
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
 </pre>
###### answer
<pre> ```python
def is_equal_to_sum_even(n):
    # Check if n is less than or equal to 0 (should return False in such cases)
    if n <= 0:
        return False
    
    # Initialize a set to store even numbers that are multiples of 2
    even_nums = {i * 2 for i in range(1, int(n / 2) + 1)}
    
    # Calculate the total sum of elements in the set
    total_sum = sum(even_nums)
    
    # Return True if the total sum equals n, otherwise False
    return total_sum == n
``` </pre>
###### canonical_solution
<pre>     return n%2 == 0 and n >= 8
 </pre>
###### test
<pre> def check(candidate):
    assert candidate(4) == False
    assert candidate(6) == False
    assert candidate(8) == True
    assert candidate(10) == True
    assert candidate(11) == False
    assert candidate(12) == True
    assert candidate(13) == False
    assert candidate(16) == True
 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 39
     35     assert candidate(13) == False
     36     assert candidate(16) == True
---> 39 check(is_equal_to_sum_even)
Cell In[1], line 31, in check(candidate)
     29 assert candidate(4) == False
     30 assert candidate(6) == False
---> 31 assert candidate(8) == True
     32 assert candidate(10) == True
     33 assert candidate(11) == False
AssertionError:  </pre>
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
def modp(n: int, p: int):
    # Initialize result with 1 to handle special case n=0
    result = 1
    # Handle negative values of n by converting them to positive
    if n < 0:
        n = -n
    # Calculate power using repeated squaring method
    while n > 0:
        # If n is odd, multiply result with p
        if n % 2 == 1:
            result = (result * p) % p
        # Square p and halve n
        p = (p * p) % p
        n //= 2
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
###### traceback
<pre> ---------------------------------------------------------------------------ZeroDivisionError                         Traceback (most recent call last)Cell In[1], line 53
     48     assert candidate(30, 5) == 4
     49     assert candidate(31, 5) == 3
---> 53 check(modp)
Cell In[1], line 43, in check(candidate)
     42 def check(candidate):
---> 43     assert candidate(3, 5) == 3
     44     assert candidate(1101, 101) == 2
     45     assert candidate(0, 101) == 1
Cell In[1], line 30, in modp(n, p)
     27 while n > 0:
     28     # If n is odd, multiply result with p
     29     if n % 2 == 1:
---> 30         result = (result * p) % p
     31     # Square p and halve n
     32     p = (p * p) % p
ZeroDivisionError: integer division or modulo by zero </pre>
