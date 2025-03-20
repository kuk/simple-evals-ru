# mbpp / saiga-yandexgpt-8b
### 11
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to remove first and last occurrence of a given character from the string.

Your code should pass these tests:

assert remove_Occ("hello","l") == "heo"
assert remove_Occ("abcda","a") == "bcd"
assert remove_Occ("PHP","P") == "H"

Your response should only contain the code for this function.

def remove_Occ(s,ch): 
    ...


 </pre>
###### answer
<pre> ```python
def remove_Occ(s, ch):
    if ch not in s:
        return s
    first_occ = s.find(ch)
    last_occ = s.rfind(ch)
    return s[:first_occ] + s[first_occ+1:last_occ] + s[last_occ+1:]
``` </pre>
###### canonical_solution
<pre> def remove_Occ(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s  </pre>
###### test
<pre> assert remove_Occ("hello","l") == "heo"
assert remove_Occ("abcda","a") == "bcd"
assert remove_Occ("PHP","P") == "H" </pre>
### 309
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the maximum of two numbers.

Your code should pass these tests:

assert maximum(5,10) == 10
assert maximum(-1,-2) == -1
assert maximum(9,7) == 9

Your response should only contain the code for this function.

def maximum(a,b):   
    ...


 </pre>
###### answer
<pre> ```python
def maximum(a,b):
    return max(a, b)
``` </pre>
###### canonical_solution
<pre> def maximum(a,b):   
    if a >= b: 
        return a 
    else: 
        return b  </pre>
###### test
<pre> assert maximum(5,10) == 10
assert maximum(-1,-2) == -1
assert maximum(9,7) == 9 </pre>
### 96
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the number of divisors of a given integer.

Your code should pass these tests:

assert divisor(15) == 4
assert divisor(12) == 6
assert divisor(9) == 3

Your response should only contain the code for this function.

def divisor(n):
    ...


 </pre>
###### answer
<pre> ```python
def divisor(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count
``` </pre>
###### canonical_solution
<pre> def divisor(n):
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x </pre>
###### test
<pre> assert divisor(15) == 4
assert divisor(12) == 6
assert divisor(9) == 3 </pre>
### 75
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find tuples which have all elements divisible by k from the given list of tuples.

Your code should pass these tests:

assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
assert find_tuples([(5, 25, 30), (4, 2, 3), (7, 8, 9)], 5) == [(5, 25, 30)]
assert find_tuples([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == [(8, 16, 4)]

Your response should only contain the code for this function.

def find_tuples(test_list, K):
    ...


 </pre>
###### answer
<pre> ```python
def find_tuples(test_list, K):
    return [t for t in test_list if all(x % K == 0 for x in t)]
``` </pre>
###### canonical_solution
<pre> def find_tuples(test_list, K):
  res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
  return res </pre>
###### test
<pre> assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
assert find_tuples([(5, 25, 30), (4, 2, 3), (7, 8, 9)], 5) == [(5, 25, 30)]
assert find_tuples([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == [(8, 16, 4)] </pre>
### 388
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the highest power of 2 that is less than or equal to n.

Your code should pass these tests:

assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(19) == 16
assert highest_Power_of_2(32) == 32

Your response should only contain the code for this function.

def highest_Power_of_2(n): 
    ...


 </pre>
###### answer
<pre> ```python
def highest_Power_of_2(n):
    return 2 ** (n.bit_length() - 1)
``` </pre>
###### canonical_solution
<pre> def highest_Power_of_2(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res  </pre>
###### test
<pre> assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(19) == 16
assert highest_Power_of_2(32) == 32 </pre>
### 435
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the last digit of a given number.

Your code should pass these tests:

assert last_Digit(123) == 3
assert last_Digit(25) == 5
assert last_Digit(30) == 0

Your response should only contain the code for this function.

def last_Digit(n) :
    ...


 </pre>
###### answer
<pre> ```python
def last_Digit(n):
    return n % 10
``` </pre>
###### canonical_solution
<pre> def last_Digit(n) :
    return (n % 10)  </pre>
###### test
<pre> assert last_Digit(123) == 3
assert last_Digit(25) == 5
assert last_Digit(30) == 0 </pre>
### 451
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to remove all whitespaces from the given string.

Your code should pass these tests:

assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'

Your response should only contain the code for this function.

def remove_whitespaces(text1):
    ...


 </pre>
###### answer
<pre> ```python
def remove_whitespaces(text1):
    return ''.join(char for char in text1 if not char.isspace())
``` </pre>
###### canonical_solution
<pre> import re
def remove_whitespaces(text1):
  return (re.sub(r'\s+', '',text1)) </pre>
###### test
<pre> assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift' </pre>
### 61
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to count the number of substrings with the sum of digits equal to their length.

Your code should pass these tests:

assert count_Substrings('112112') == 6
assert count_Substrings('111') == 6
assert count_Substrings('1101112') == 12

Your response should only contain the code for this function.

def count_Substrings(s):
    ...


 </pre>
###### answer
<pre> ```python
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        current_sum = 0
        for j in range(i, len(s)):
            current_sum += int(s[j])
            if current_sum == j - i + 1:
                count += 1
    return count
``` </pre>
###### canonical_solution
<pre> from collections import defaultdict
def count_Substrings(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count </pre>
###### test
<pre> assert count_Substrings('112112') == 6
assert count_Substrings('111') == 6
assert count_Substrings('1101112') == 12 </pre>
### 397
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the median of three numbers.

Your code should pass these tests:

assert median_numbers(25,55,65)==55.0
assert median_numbers(20,10,30)==20.0
assert median_numbers(15,45,75)==45.0

Your response should only contain the code for this function.

def median_numbers(a,b,c):
    ...


 </pre>
###### answer
<pre> ```python
def median_numbers(a, b, c):
    return sorted([a, b, c])[1]
``` </pre>
###### canonical_solution
<pre> def median_numbers(a,b,c):
 if a > b:
    if a &lt; c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b &lt; c:
        median = b
    else:
        median = c
 return median </pre>
###### test
<pre> assert median_numbers(25,55,65)==55.0
assert median_numbers(20,10,30)==20.0
assert median_numbers(15,45,75)==45.0 </pre>
### 308
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.

Your code should pass these tests:

assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]

Your response should only contain the code for this function.

def large_product(nums1, nums2, N):
    ...


 </pre>
###### answer
<pre> ```python
def large_product(nums1, nums2, N):
    # Create a list of tuples (product, num1, num2)
    products = [(a * b, a, b) for a in nums1 for b in nums2]
    # Sort the products in descending order
    products.sort(reverse=True)
    # Extract the top N products
    return [product for product, _, _ in products[:N]]
``` </pre>
###### canonical_solution
<pre> def large_product(nums1, nums2, N):
    result = sorted([x*y for x in nums1 for y in nums2], reverse=True)[:N]
    return result </pre>
###### test
<pre> assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45] </pre>
