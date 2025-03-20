# humaneval / ruadapt-qwen-pro-32b
### HumanEval/63
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
 </pre>
###### answer
<pre> ```python
def fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Используем динамическое программирование для оптимизации
    fibfib_values = [0, 0, 1] + [0] * (n - 2)
    
    for i in range(3, n + 1):
        fibfib_values[i] = fibfib_values[i-1] + fibfib_values[i-2] + fibfib_values[i-3]
    
    return fibfib_values[n]
```

Этот код использует динамическое программирование для эффективного вычисления n-го элемента последовательности FibFib, что позволяет избежать избыточных вычислений, характерных для рекурсивного подхода. </pre>
###### canonical_solution
<pre>     if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate(2) == 1
    assert candidate(1) == 0
    assert candidate(5) == 4
    assert candidate(8) == 24
    assert candidate(10) == 81
    assert candidate(12) == 274
    assert candidate(14) == 927

 </pre>
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
def is_prime(n):
    """Check if a number is prime."""
    if n &lt;= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    """
    return is_prime(len(string))

# Examples
print(prime_length('Hello'))   # == True
print(prime_length('abcdcba')) # == True
print(prime_length('kittens')) # == True
print(prime_length('orange'))  # == False
```
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
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert the number to a positive and then to a string to iterate over digits
    digits = str(abs(num))
    
    even_count = 0
    odd_count = 0
    
    for digit in digits:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return (even_count, odd_count)
```
 </pre>
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
### HumanEval/96
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
 </pre>
###### answer
<pre> ```python
def is_prime(num):
    if num &lt;= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
            if len(primes) == n:
                break
    return primes
```
``` </pre>
###### canonical_solution
<pre>     primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

 </pre>
###### test
<pre> def check(candidate):

    assert candidate(5) == [2,3]
    assert candidate(6) == [2,3,5]
    assert candidate(7) == [2,3,5]
    assert candidate(10) == [2,3,5,7]
    assert candidate(0) == []
    assert candidate(22) == [2,3,5,7,11,13,17,19]
    assert candidate(1) == []
    assert candidate(18) == [2,3,5,7,11,13,17]
    assert candidate(47) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    assert candidate(101) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

 </pre>
### HumanEval/119
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
 </pre>
###### answer
<pre> ```python
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
    '''
    def is_good(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
                if balance &lt; 0:
                    return False
        return balance == 0

    s1, s2 = lst
    open1, close1 = s1.count('('), s1.count(')')
    open2, close2 = s2.count('('), s2.count(')')

    # Check both possible concatenations
    if (open1 + open2 == close1 + close2 and
        is_good(s1 + s2) or is_good(s2 + s1)):
        return 'Yes'
    return 'No'
```
``` </pre>
###### canonical_solution
<pre>     def check(s):
        val = 0
        for i in s:
            if i == '(':
                val = val + 1
            else:
                val = val - 1
            if val &lt; 0:
                return False
        return True if val == 0 else False

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'Yes' if check(S1) or check(S2) else 'No'
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(['()(', ')']) == 'Yes'
    assert candidate([')', ')']) == 'No'
    assert candidate(['(()(())', '())())']) == 'No'
    assert candidate([')())', '(()()(']) == 'Yes'
    assert candidate(['(())))', '(()())((']) == 'Yes'
    assert candidate(['()', '())']) == 'No'
    assert candidate(['(()(', '()))()']) == 'Yes'
    assert candidate(['((((', '((())']) == 'No'
    assert candidate([')(()', '(()(']) == 'No'
    assert candidate([')(', ')(']) == 'No'
    

    # Check some edge cases that are easy to work out by hand.
    assert candidate(['(', ')']) == 'Yes'
    assert candidate([')', '(']) == 'Yes' 

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
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Начальное максимальное простое число
    largest_prime = -1
    
    # Разделить n на 2, пока оно четное
    while n % 2 == 0:
        largest_prime = 2
        n //= 2
    
    # Проверить делители начиная с 3
    factor = 3
    while factor * factor &lt;= n:
        while n % factor == 0:
            largest_prime = factor
            n //= factor
        factor += 2
    
    # Если n осталось больше 2, оно является простым числом
    if n > 2:
        largest_prime = n
    
    return largest_prime
``` </pre>
###### canonical_solution
<pre>     def is_prime(k):
        if k &lt; 2:
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
### HumanEval/71
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
 </pre>
###### answer
<pre> ```python
def triangle_area(a, b, c):
    # Check if the sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1
``` </pre>
###### canonical_solution
<pre>     if a + b &lt;= c or a + c &lt;= b or b + c &lt;= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(3, 4, 5) == 6.00, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1, 2, 10) == -1
    assert candidate(4, 8, 5) == 8.18
    assert candidate(2, 2, 2) == 1.73
    assert candidate(1, 2, 3) == -1
    assert candidate(10, 5, 7) == 16.25
    assert candidate(2, 6, 3) == -1

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 1, 1) == 0.43, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(2, 2, 10) == -1

 </pre>
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
    # Count the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # Count the number of even elements in lst2
    even_count = sum(1 for num in lst2 if num % 2 == 0)
    
    # If there are enough even numbers in lst2 to replace all odd numbers in lst1, return "YES"
    if even_count >= odd_count:
        return "YES"
    else:
        return "NO"
```

This implementation first counts the number of odd elements in `lst1` and the number of even elements in `lst2`. If there are at least as many even numbers in `lst2` as there are odd numbers in `lst1`, it is possible to make all elements of `lst1` even by exchanging elements, so it returns "YES". Otherwise, it returns "NO". </pre>
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
### HumanEval/161
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
 </pre>
###### answer
<pre> ```python
def solve(s):
    # Check if the string contains any letters
    if any(c.isalpha() for c in s):
        # Reverse the case of each letter in the string
        return ''.join(c.swapcase() if c.isalpha() else c for c in s)
    else:
        # If no letters are present, reverse the entire string
        return s[::-1]
```
``` </pre>
###### canonical_solution
<pre>     flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate("AsDf") == "aSdF"
    assert candidate("1234") == "4321"
    assert candidate("ab") == "AB"
    assert candidate("#a@C") == "#A@c"
    assert candidate("#AsdfW^45") == "#aSDFw^45"
    assert candidate("#6@2") == "2@6#"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("#$a^D") == "#$A^d"
    assert candidate("#ccc") == "#CCC"

    # Don't remove this line:
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
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10."""
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    
    return ''.join(digits[::-1])
```
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
