# mbpp / yandexgpt-4-lite
### 421
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to concatenate each element of tuple by the delimiter.

Your code should pass these tests:

assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

Your response should only contain the code for this function.

def concatenate_tuple(test_tup):
    ...


 </pre>
###### answer
<pre> ```
def concatenate_tuple(test_tup):
    result = ''
    for element in test_tup:
        result += element + '-'
    return result[:-1]  # Удаляем последний символ '-'
``` </pre>
###### canonical_solution
<pre> def concatenate_tuple(test_tup):
    delim = "-"
    res = ''.join([str(ele) + delim for ele in test_tup])
    res = res[ : len(res) - len(delim)]
    return (str(res))  </pre>
###### test
<pre> assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP' </pre>
###### traceback
<pre> ---------------------------------------------------------------------------TypeError                                 Traceback (most recent call last)Cell In[1], line 14
     10         result += element + '-'
     11     return result[:-1]  # Удаляем последний символ '-'
---> 14 assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
     15 assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
     16 assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'
Cell In[1], line 10, in concatenate_tuple(test_tup)
      8 result = ''
      9 for element in test_tup:
---> 10     result += element + '-'
     11 return result[:-1]  # Удаляем последний символ '-'
TypeError: unsupported operand type(s) for +: 'int' and 'str' </pre>
### 445
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to perform index wise multiplication of tuple elements in the given two tuples.

Your code should pass these tests:

assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
assert index_multiplication(((2, 4), (5, 6), (3, 10), (2, 11)),((7, 8), (4, 10), (2, 2), (8, 4)) ) == ((14, 32), (20, 60), (6, 20), (16, 44))
assert index_multiplication(((3, 5), (6, 7), (4, 11), (3, 12)),((8, 9), (5, 11), (3, 3), (9, 5)) ) == ((24, 45), (30, 77), (12, 33), (27, 60))

Your response should only contain the code for this function.

def index_multiplication(test_tup1, test_tup2):
    ...


 </pre>
###### answer
<pre> ```
def index_multiplication(test_tup1, test_tup2):
    result = []
    for i in range(len(test_tup1)):
        result.append(test_tup1[i] * test_tup2[i])
    return result
``` </pre>
###### canonical_solution
<pre> def index_multiplication(test_tup1, test_tup2):
  res = tuple(tuple(a * b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res)  </pre>
###### test
<pre> assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
assert index_multiplication(((2, 4), (5, 6), (3, 10), (2, 11)),((7, 8), (4, 10), (2, 2), (8, 4)) ) == ((14, 32), (20, 60), (6, 20), (16, 44))
assert index_multiplication(((3, 5), (6, 7), (4, 11), (3, 12)),((8, 9), (5, 11), (3, 3), (9, 5)) ) == ((24, 45), (30, 77), (12, 33), (27, 60)) </pre>
###### traceback
<pre> ---------------------------------------------------------------------------TypeError                                 Traceback (most recent call last)Cell In[1], line 14
     10         result.append(test_tup1[i] * test_tup2[i])
     11     return result
---> 14 assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
     15 assert index_multiplication(((2, 4), (5, 6), (3, 10), (2, 11)),((7, 8), (4, 10), (2, 2), (8, 4)) ) == ((14, 32), (20, 60), (6, 20), (16, 44))
     16 assert index_multiplication(((3, 5), (6, 7), (4, 11), (3, 12)),((8, 9), (5, 11), (3, 3), (9, 5)) ) == ((24, 45), (30, 77), (12, 33), (27, 60))
Cell In[1], line 10, in index_multiplication(test_tup1, test_tup2)
      8 result = []
      9 for i in range(len(test_tup1)):
---> 10     result.append(test_tup1[i] * test_tup2[i])
     11 return result
TypeError: can't multiply sequence by non-int of type 'tuple' </pre>
### 443
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the largest negative number from the given list.

Your code should pass these tests:

assert largest_neg([1,2,3,-4,-6]) == -6
assert largest_neg([1,2,3,-8,-9]) == -9
assert largest_neg([1,2,3,4,-1]) == -1

Your response should only contain the code for this function.

def largest_neg(list1): 
    ...


 </pre>
###### answer
<pre> ```
def largest_neg(list1):
    max_neg = float('-inf')
    for num in list1:
        if num &lt; 0 and num > max_neg:
            max_neg = num
    return max_neg
``` </pre>
###### canonical_solution
<pre> def largest_neg(list1): 
    max = list1[0] 
    for x in list1: 
        if x &lt; max : 
             max = x  
    return max </pre>
###### test
<pre> assert largest_neg([1,2,3,-4,-6]) == -6
assert largest_neg([1,2,3,-8,-9]) == -9
assert largest_neg([1,2,3,4,-1]) == -1 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 15
     11             max_neg = num
     12     return max_neg
---> 15 assert largest_neg([1,2,3,-4,-6]) == -6
     16 assert largest_neg([1,2,3,-8,-9]) == -9
     17 assert largest_neg([1,2,3,4,-1]) == -1
AssertionError:  </pre>
### 461
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to count the upper case characters in a given string.

Your code should pass these tests:

assert upper_ctr('PYthon') == 1
assert upper_ctr('BigData') == 1
assert upper_ctr('program') == 0

Your response should only contain the code for this function.

def upper_ctr(str):
    ...


 </pre>
###### answer
<pre> ```
def upper_ctr(str):
    upper_case_chars = 0
    for char in str:
        if char.isupper():
            upper_case_chars += 1
    return upper_case_chars
``` </pre>
###### canonical_solution
<pre> def upper_ctr(str):
    upper_ctr = 0
    for i in range(len(str)):
          if str[i] >= 'A' and str[i] &lt;= 'Z': upper_ctr += 1
          return upper_ctr </pre>
###### test
<pre> assert upper_ctr('PYthon') == 1
assert upper_ctr('BigData') == 1
assert upper_ctr('program') == 0 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 15
     11             upper_case_chars += 1
     12     return upper_case_chars
---> 15 assert upper_ctr('PYthon') == 1
     16 assert upper_ctr('BigData') == 1
     17 assert upper_ctr('program') == 0
AssertionError:  </pre>
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
<pre> ```
def remove_Occ(s, ch):
    # Находим первое и последнее вхождения символа ch в строку s
    first_index = s.find(ch)
    last_index = s.rfind(ch)

    # Если первое и последнее вхождения совпадают, удаляем только одно из них
    if first_index == last_index:
        s = s[:first_index] + s[first_index + 1:]

    # Иначе удаляем оба вхождения
    else:
        s = s[:first_index] + s[first_index + 1:last_index] + s[last_index:]

    return s
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
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 23
     18         s = s[:first_index] + s[first_index + 1:last_index] + s[last_index:]
     20     return s
---> 23 assert remove_Occ("hello","l") == "heo"
     24 assert remove_Occ("abcda","a") == "bcd"
     25 assert remove_Occ("PHP","P") == "H"
AssertionError:  </pre>
### 129
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to calculate whether the matrix is a magic square.

Your code should pass these tests:

assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

Your response should only contain the code for this function.

def magic_square_test(my_matrix):
    ...


 </pre>
###### answer
<pre> ```
def magic_square_test(my_matrix):
    n = len(my_matrix)
    if n != n**2:
        return False

    for i in range(n):
        sum_row = 0
        for j in range(n):
            sum_row += my_matrix[i][j]

        if sum_row != (n**2 + 1) // 2:
            return False

    return True
``` </pre>
###### canonical_solution
<pre> def magic_square_test(my_matrix):
    iSize = len(my_matrix[0])
    sum_list = []
    sum_list.extend([sum (lines) for lines in my_matrix])   
    for col in range(iSize):
        sum_list.append(sum(row[col] for row in my_matrix))
    result1 = 0
    for i in range(0,iSize):
        result1 +=my_matrix[i][i]
    sum_list.append(result1)      
    result2 = 0
    for i in range(iSize-1,-1,-1):
        result2 +=my_matrix[i][i]
    sum_list.append(result2)
    if len(set(sum_list))>1:
        return False
    return True </pre>
###### test
<pre> assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 23
     18             return False
     20     return True
---> 23 assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
     24 assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
     25 assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False
AssertionError:  </pre>
### 453
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the sum of even factors of a number.

Your code should pass these tests:

assert sumofFactors(18) == 26
assert sumofFactors(30) == 48
assert sumofFactors(6) == 8

Your response should only contain the code for this function.

def sumofFactors(n) : 
    ...


 </pre>
###### answer
<pre> ```
def sumofFactors(n):
    factors = []
    for i in range(2, n+1):
        if n % i == 0:
            factors.append(i)
    return sum(factors)
``` </pre>
###### canonical_solution
<pre> import math 
def sumofFactors(n) : 
    if (n % 2 != 0) : 
        return 0
    res = 1
    for i in range(2, (int)(math.sqrt(n)) + 1) :    
        count = 0
        curr_sum = 1
        curr_term = 1
        while (n % i == 0) : 
            count= count + 1
            n = n // i 
            if (i == 2 and count == 1) : 
                curr_sum = 0
            curr_term = curr_term * i 
            curr_sum = curr_sum + curr_term 
        res = res * curr_sum  
    if (n >= 2) : 
        res = res * (1 + n) 
    return res </pre>
###### test
<pre> assert sumofFactors(18) == 26
assert sumofFactors(30) == 48
assert sumofFactors(6) == 8 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 15
     11             factors.append(i)
     12     return sum(factors)
---> 15 assert sumofFactors(18) == 26
     16 assert sumofFactors(30) == 48
     17 assert sumofFactors(6) == 8
AssertionError:  </pre>
### 56
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to check if a given number is one less than twice its reverse.

Your code should pass these tests:

assert check(70) == False
assert check(23) == False
assert check(73) == True

Your response should only contain the code for this function.

def rev(num):    
    ...


 </pre>
###### answer
<pre> ```
def check(num):
    reverse_num = rev(num)
    return reverse_num == 2 * num - 1

def rev(num):
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num //= 10
    return result
``` </pre>
###### canonical_solution
<pre> def rev(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num // 10  
    return rev_num  
def check(n):    
    return (2 * rev(n) == n + 1)   </pre>
###### test
<pre> assert check(70) == False
assert check(23) == False
assert check(73) == True </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 21
     19 assert check(70) == False
     20 assert check(23) == False
---> 21 assert check(73) == True
AssertionError:  </pre>
### 72
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to check whether the given number can be represented as the difference of two squares or not.

Your code should pass these tests:

assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(15) == True

Your response should only contain the code for this function.

def dif_Square(n): 
    ...


 </pre>
###### answer
<pre> ```
def dif_Square(n):
    # Проверяем, является ли число полным квадратом
    if n % 2 == 0 and n ** 0.5 % 1 == 0:
        return True
    else:
        # Проверяем возможность представления числа как разности квадратов
        for i in range(int(n ** 0.5)):
            if n == i ** 2 - (i + 1) ** 2:
                return True
        return False
``` </pre>
###### canonical_solution
<pre> def dif_Square(n): 
    if (n % 4 != 2): 
        return True
    return False </pre>
###### test
<pre> assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(15) == True </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 19
     15                 return True
     16         return False
---> 19 assert dif_Square(5) == True
     20 assert dif_Square(10) == False
     21 assert dif_Square(15) == True
AssertionError:  </pre>
### 252
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to convert complex numbers to polar coordinates.

Your code should pass these tests:

assert convert(1) == (1.0, 0.0)
assert convert(4) == (4.0,0.0)
assert convert(5) == (5.0,0.0)

Your response should only contain the code for this function.

def convert(numbers):    
    ...


 </pre>
###### answer
<pre> ```
def convert(numbers):
    if isinstance(numbers, complex):
        magnitude = abs(numbers)
        angle = math.atan2(numbers.imag, numbers.real)
        return magnitude, angle
    else:
        return None
``` </pre>
###### canonical_solution
<pre> import cmath  
def convert(numbers):    
  num = cmath.polar(numbers)  
  return (num)  </pre>
###### test
<pre> assert convert(1) == (1.0, 0.0)
assert convert(4) == (4.0,0.0)
assert convert(5) == (5.0,0.0) </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 16
     12     else:
     13         return None
---> 16 assert convert(1) == (1.0, 0.0)
     17 assert convert(4) == (4.0,0.0)
     18 assert convert(5) == (5.0,0.0)
AssertionError:  </pre>
### 131
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to reverse only the vowels of a given string (where y is not a vowel).

Your code should pass these tests:

assert reverse_vowels("Python") == "Python"
assert reverse_vowels("USA") == "ASU"
assert reverse_vowels("ab") == "ab"

Your response should only contain the code for this function.

def reverse_vowels(str1):
    ...


 </pre>
###### answer
<pre> ```
def reverse_vowels(str1):
    result = ""
    for char in str1:
        if char in "aeiouy":
            result += char[::-1]
        else:
            result += char
    return result
``` </pre>
###### canonical_solution
<pre> def reverse_vowels(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string </pre>
###### test
<pre> assert reverse_vowels("Python") == "Python"
assert reverse_vowels("USA") == "ASU"
assert reverse_vowels("ab") == "ab" </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 18
     14     return result
     17 assert reverse_vowels("Python") == "Python"
---> 18 assert reverse_vowels("USA") == "ASU"
     19 assert reverse_vowels("ab") == "ab"
AssertionError:  </pre>
### 239
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.

Your code should pass these tests:

assert get_total_number_of_sequences(10, 4) == 4
assert get_total_number_of_sequences(5, 2) == 6
assert get_total_number_of_sequences(16, 3) == 84

Your response should only contain the code for this function.

def get_total_number_of_sequences(m,n): 
    ...


 </pre>
###### answer
<pre> ```
def get_total_number_of_sequences(m, n):
    # Инициализируем количество возможных последовательностей как 1
    count = 1

    # Проходим по всем возможным начальным элементам последовательности
    for start in range(m // 2 + 3):
        # Проверяем, что длина последовательности не превышает n
        if n > 0:
            # Создаем последовательность, начиная с start и добавляя к каждому элементу условие, что он должен быть больше или равен удвоенному предыдущему элементу и меньше или равен m
            sequence = [start]
            for i in range(n - 1):
                if sequence[-1] &lt; m and sequence[-1] * 2 &lt;= sequence[-2]:
                    sequence.append(sequence[-1] * 2)
                else:
                    break
            if sequence[-1] &lt;= m:
                count += 1

    return count
``` </pre>
###### canonical_solution
<pre> def get_total_number_of_sequences(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i&lt;j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n] </pre>
###### test
<pre> assert get_total_number_of_sequences(10, 4) == 4
assert get_total_number_of_sequences(5, 2) == 6
assert get_total_number_of_sequences(16, 3) == 84 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------IndexError                                Traceback (most recent call last)Cell In[1], line 28
     23                 count += 1
     25     return count
---> 28 assert get_total_number_of_sequences(10, 4) == 4
     29 assert get_total_number_of_sequences(5, 2) == 6
     30 assert get_total_number_of_sequences(16, 3) == 84
Cell In[1], line 18, in get_total_number_of_sequences(m, n)
     16 sequence = [start]
     17 for i in range(n - 1):
---> 18     if sequence[-1] &lt; m and sequence[-1] * 2 &lt;= sequence[-2]:
     19         sequence.append(sequence[-1] * 2)
     20     else:
IndexError: list index out of range </pre>
### 293
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the third side of a right angled triangle.

Your code should pass these tests:

assert otherside_rightangle(7,8)==10.63014581273465
assert otherside_rightangle(3,4)==5
assert otherside_rightangle(7,15)==16.55294535724685

Your response should only contain the code for this function.

def otherside_rightangle(w,h):
    ...


 </pre>
###### answer
<pre> ```
def otherside_rightangle(w, h):
    # Используем теорему Пифагора для нахождения третьей стороны
    return math.sqrt(w**2 + h**2)
``` </pre>
###### canonical_solution
<pre> import math
def otherside_rightangle(w,h):
  s=math.sqrt((w*w)+(h*h))
  return s </pre>
###### test
<pre> assert otherside_rightangle(7,8)==10.63014581273465
assert otherside_rightangle(3,4)==5
assert otherside_rightangle(7,15)==16.55294535724685 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)Cell In[1], line 12
      7 def otherside_rightangle(w, h):
      8     # Используем теорему Пифагора для нахождения третьей стороны
      9     return math.sqrt(w**2 + h**2)
---> 12 assert otherside_rightangle(7,8)==10.63014581273465
     13 assert otherside_rightangle(3,4)==5
     14 assert otherside_rightangle(7,15)==16.55294535724685
Cell In[1], line 9, in otherside_rightangle(w, h)
      7 def otherside_rightangle(w, h):
      8     # Используем теорему Пифагора для нахождения третьей стороны
----> 9     return math.sqrt(w**2 + h**2)
NameError: name 'math' is not defined </pre>
### 434
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that matches a string that has an a followed by one or more b's.

Your code should pass these tests:

assert text_match_one("ac")==False
assert text_match_one("dc")==False
assert text_match_one("abba")==True

Your response should only contain the code for this function.

def text_match_one(text):
    ...


 </pre>
###### answer
<pre> ```
def text_match_one(text):
    return 'a' in text and text.count('a') == 1 and text.count('b') > 0
``` </pre>
###### canonical_solution
<pre> import re
def text_match_one(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return True
        else:
                return False
 </pre>
###### test
<pre> assert text_match_one("ac")==False
assert text_match_one("dc")==False
assert text_match_one("abba")==True </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 13
     11 assert text_match_one("ac")==False
     12 assert text_match_one("dc")==False
---> 13 assert text_match_one("abba")==True
AssertionError:  </pre>
### 123
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to sum all amicable numbers from 1 to a specified number.

Your code should pass these tests:

assert amicable_numbers_sum(999)==504
assert amicable_numbers_sum(9999)==31626
assert amicable_numbers_sum(99)==0

Your response should only contain the code for this function.

def amicable_numbers_sum(limit):
    ...


 </pre>
###### answer
<pre> ```
def amicable_numbers_sum(limit):
    amicable_numbers = []
    for i in range(1, limit+1):
        if is_amicable(i):
            amicable_numbers.append(i)
    return sum(amicable_numbers)

def is_amicable(n):
    # Проверяем, является ли число дружественным
    # Дружественные числа — это пары чисел, где каждое из них равно сумме всех делителей другого числа, кроме самого себя
    divisors_sum = sum(divisors(n))
    return divisors_sum == n

def divisors(n):
    # Возвращаем список делителей числа n
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors
``` </pre>
###### canonical_solution
<pre> def amicable_numbers_sum(limit):
    if not isinstance(limit, int):
        return "Input is not an integer!"
    if limit &lt; 1:
        return "Input must be bigger than 0!"
    amicables = set()
    for num in range(2, limit+1):
        if num in amicables:
            continue
        sum_fact = sum([fact for fact in range(1, num) if num % fact == 0])
        sum_fact2 = sum([fact for fact in range(1, sum_fact) if sum_fact % fact == 0])
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)
    return sum(amicables) </pre>
###### test
<pre> assert amicable_numbers_sum(999)==504
assert amicable_numbers_sum(9999)==31626
assert amicable_numbers_sum(99)==0 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 29
     25             divisors.append(i)
     26     return divisors
---> 29 assert amicable_numbers_sum(999)==504
     30 assert amicable_numbers_sum(9999)==31626
     31 assert amicable_numbers_sum(99)==0
AssertionError:  </pre>
### 271
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.

Your code should pass these tests:

assert even_Power_Sum(2) == 1056
assert even_Power_Sum(3) == 8832
assert even_Power_Sum(1) == 32

Your response should only contain the code for this function.

def even_Power_Sum(n): 
    ...


 </pre>
###### answer
<pre> ```
def even_Power_Sum(n):
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += pow(i, 5)
    return sum
``` </pre>
###### canonical_solution
<pre> def even_Power_Sum(n): 
    sum = 0; 
    for i in range(1,n+1): 
        j = 2*i; 
        sum = sum + (j*j*j*j*j); 
    return sum;  </pre>
###### test
<pre> assert even_Power_Sum(2) == 1056
assert even_Power_Sum(3) == 8832
assert even_Power_Sum(1) == 32 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 15
     11             sum += pow(i, 5)
     12     return sum
---> 15 assert even_Power_Sum(2) == 1056
     16 assert even_Power_Sum(3) == 8832
     17 assert even_Power_Sum(1) == 32
AssertionError:  </pre>
### 84
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the nth number in the newman conway sequence.

Your code should pass these tests:

assert sequence(10) == 6
assert sequence(2) == 1
assert sequence(3) == 2

Your response should only contain the code for this function.

def sequence(n): 
    ...


 </pre>
###### answer
<pre> ```
def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        previous = 0
        for i in range(n-2):
            previous = previous + i + 3
        return previous + n - 2
``` </pre>
###### canonical_solution
<pre> def sequence(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1)) </pre>
###### test
<pre> assert sequence(10) == 6
assert sequence(2) == 1
assert sequence(3) == 2 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 19
     15             previous = previous + i + 3
     16         return previous + n - 2
---> 19 assert sequence(10) == 6
     20 assert sequence(2) == 1
     21 assert sequence(3) == 2
AssertionError:  </pre>
### 432
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the median length of a trapezium.

Your code should pass these tests:

assert median_trapezium(15,25,35)==20
assert median_trapezium(10,20,30)==15
assert median_trapezium(6,9,4)==7.5

Your response should only contain the code for this function.

def median_trapezium(base1,base2,height):
    ...


 </pre>
###### answer
<pre> ```
def median_trapezium(base1, base2, height):
    # Находим полупериметр trapezium
    perimeter = (base1 + base2) / 2

    # Вычисляем среднюю длину основания
    mid_base = perimeter - height

    return mid_base
``` </pre>
###### canonical_solution
<pre> def median_trapezium(base1,base2,height):
 median = 0.5 * (base1+ base2)
 return median </pre>
###### test
<pre> assert median_trapezium(15,25,35)==20
assert median_trapezium(10,20,30)==15
assert median_trapezium(6,9,4)==7.5 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 17
     12     mid_base = perimeter - height
     14     return mid_base
---> 17 assert median_trapezium(15,25,35)==20
     18 assert median_trapezium(10,20,30)==15
     19 assert median_trapezium(6,9,4)==7.5
AssertionError:  </pre>
### 311
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to set the left most unset bit.

Your code should pass these tests:

assert set_left_most_unset_bit(10) == 14
assert set_left_most_unset_bit(12) == 14
assert set_left_most_unset_bit(15) == 15

Your response should only contain the code for this function.

def set_left_most_unset_bit(n): 
    ...


 </pre>
###### answer
<pre> ```
def set_left_most_unset_bit(n):
    # Переводим число в двоичное представление
    binary = bin(n)[2:]

    # Находим индекс первого не установленного бита
    index = binary.find('0')

    # Возвращаем число с установленным левым битом
    return int(binary[:index + 1] + '1', 2)
``` </pre>
###### canonical_solution
<pre> def set_left_most_unset_bit(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 &lt;&lt; (pos)))  </pre>
###### test
<pre> assert set_left_most_unset_bit(10) == 14
assert set_left_most_unset_bit(12) == 14
assert set_left_most_unset_bit(15) == 15 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 18
     14     # Возвращаем число с установленным левым битом
     15     return int(binary[:index + 1] + '1', 2)
---> 18 assert set_left_most_unset_bit(10) == 14
     19 assert set_left_most_unset_bit(12) == 14
     20 assert set_left_most_unset_bit(15) == 15
AssertionError:  </pre>
### 295
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to return the sum of all divisors of a number.

Your code should pass these tests:

assert sum_div(8)==7
assert sum_div(12)==16
assert sum_div(7)==1

Your response should only contain the code for this function.

def sum_div(number):
    ...


 </pre>
###### answer
<pre> ```
def sum_div(number):
    divisors = set()
    for i in range(1, number+1):
        if number % i == 0:
            divisors.add(i)
    return sum(divisors)
``` </pre>
###### canonical_solution
<pre> def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors) </pre>
###### test
<pre> assert sum_div(8)==7
assert sum_div(12)==16
assert sum_div(7)==1 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 15
     11             divisors.add(i)
     12     return sum(divisors)
---> 15 assert sum_div(8)==7
     16 assert sum_div(12)==16
     17 assert sum_div(7)==1
AssertionError:  </pre>
