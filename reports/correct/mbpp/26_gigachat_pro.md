# mbpp / gigachat-2-pro
### 119
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the element that appears only once in a sorted array.

Your code should pass these tests:

assert search([1,1,2,2,3]) == 3
assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
assert search([1,2,2,3,3,4,4]) == 1

Your response should only contain the code for this function.

def search(arr):
    ...


 </pre>
###### answer
<pre> ```python
def search(arr):
    left = 0
    right = len(arr) - 1
    
    while left &lt; right:
        mid = (left + right) // 2
        
        # Check if mid is even or odd
        if mid % 2 == 0:
            if arr[mid] == arr[mid+1]:
                left = mid + 2
            else:
                right = mid
        else:
            if arr[mid] == arr[mid-1]:
                left = mid + 1
            else:
                right = mid - 1
                
    return arr[left]
``` </pre>
###### canonical_solution
<pre> def search(arr):
    n = len(arr)
    XOR = 0
    for i in range(n) :
        XOR = XOR ^ arr[i]
    return (XOR) </pre>
###### test
<pre> assert search([1,1,2,2,3]) == 3
assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
assert search([1,2,2,3,3,4,4]) == 1 </pre>
### 140
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to flatten the list of lists into a single set of numbers.

Your code should pass these tests:

assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
assert set(extract_singly([(1, 2, 3), (4, 2, 3), (7, 8)])) == set([1, 2, 3, 4, 7, 8])
assert set(extract_singly([(7, 8, 9), (10, 11, 12), (10, 11)])) == set([7, 8, 9, 10, 11, 12])

Your response should only contain the code for this function.

def extract_singly(test_list):
    ...


 </pre>
###### answer
<pre> ```python
def extract_singly(test_list):
    return {num for sublist in test_list for num in sublist}
``` </pre>
###### canonical_solution
<pre> def extract_singly(test_list):
  res = []
  temp = set()
  for inner in test_list:
    for ele in inner:
      if not ele in temp:
        temp.add(ele)
        res.append(ele)
  return (res)  </pre>
###### test
<pre> assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
assert set(extract_singly([(1, 2, 3), (4, 2, 3), (7, 8)])) == set([1, 2, 3, 4, 7, 8])
assert set(extract_singly([(7, 8, 9), (10, 11, 12), (10, 11)])) == set([7, 8, 9, 10, 11, 12]) </pre>
### 474
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to replace characters in a string.

Your code should pass these tests:

assert replace_char("polygon",'y','l')==("pollgon")
assert replace_char("character",'c','a')==("aharaater")
assert replace_char("python",'l','a')==("python")

Your response should only contain the code for this function.

def replace_char(str1,ch,newch):
    ...


 </pre>
###### answer
<pre> ```python
def replace_char(str1, ch, newch):
    return str1.replace(ch, newch)
``` </pre>
###### canonical_solution
<pre> def replace_char(str1,ch,newch):
 str2 = str1.replace(ch, newch)
 return str2 </pre>
###### test
<pre> assert replace_char("polygon",'y','l')==("pollgon")
assert replace_char("character",'c','a')==("aharaater")
assert replace_char("python",'l','a')==("python") </pre>
### 406
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find whether the parity of a given number is odd.

Your code should pass these tests:

assert find_Parity(12) == False
assert find_Parity(7) == True
assert find_Parity(10) == False

Your response should only contain the code for this function.

def find_Parity(x): 
    ...


 </pre>
###### answer
<pre> ```python
def find_Parity(x):
    return x % 2 != 0
``` </pre>
###### canonical_solution
<pre> def find_Parity(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False </pre>
###### test
<pre> assert find_Parity(12) == False
assert find_Parity(7) == True
assert find_Parity(10) == False </pre>
### 422
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the average of cubes of first n natural numbers.

Your code should pass these tests:

assert find_Average_Of_Cube(2) == 4.5
assert find_Average_Of_Cube(3) == 12
assert find_Average_Of_Cube(1) == 1

Your response should only contain the code for this function.

def find_Average_Of_Cube(n):  
    ...


 </pre>
###### answer
<pre> ```python
def find_Average_Of_Cube(n):
    total = sum(i**3 for i in range(1, n+1))
    return total / n
``` </pre>
###### canonical_solution
<pre> def find_Average_Of_Cube(n):  
    sum = 0
    for i in range(1, n + 1): 
        sum += i * i * i  
    return round(sum / n, 6)  </pre>
###### test
<pre> assert find_Average_Of_Cube(2) == 4.5
assert find_Average_Of_Cube(3) == 12
assert find_Average_Of_Cube(1) == 1 </pre>
### 118
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to convert a string to a list of strings split on the space character.

Your code should pass these tests:

assert string_to_list("python programming")==['python','programming']
assert string_to_list("lists tuples strings")==['lists','tuples','strings']
assert string_to_list("write a program")==['write','a','program']

Your response should only contain the code for this function.

def string_to_list(string): 
    ...


 </pre>
###### answer
<pre> ```python
def string_to_list(string):
    return string.split()
``` </pre>
###### canonical_solution
<pre> def string_to_list(string): 
    lst = list(string.split(" ")) 
    return lst </pre>
###### test
<pre> assert string_to_list("python programming")==['python','programming']
assert string_to_list("lists tuples strings")==['lists','tuples','strings']
assert string_to_list("write a program")==['write','a','program'] </pre>
### 428
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to sort the given array by using shell sort.

Your code should pass these tests:

assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
assert shell_sort([24, 22, 39, 34, 87, 73, 68]) == [22, 24, 34, 39, 68, 73, 87]
assert shell_sort([32, 30, 16, 96, 82, 83, 74]) == [16, 30, 32, 74, 82, 83, 96]

Your response should only contain the code for this function.

def shell_sort(my_list):
    ...


 </pre>
###### answer
<pre> ```python
def shell_sort(my_list):
    n = len(my_list)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = my_list[i]
            j = i
            
            # Shift earlier gap-sorted elements up until the correct location for my_list[i] is found
            while j >= gap and my_list[j - gap] > temp:
                my_list[j] = my_list[j - gap]
                j -= gap
                
            # Put temp (the original my_list[i]) in its correct location
            my_list[j] = temp
        
        # Reduce the gap for the next element
        gap //= 2
    
    return my_list
``` </pre>
###### canonical_solution
<pre> def shell_sort(my_list):
    gap = len(my_list) // 2
    while gap > 0:
        for i in range(gap, len(my_list)):
            current_item = my_list[i]
            j = i
            while j >= gap and my_list[j - gap] > current_item:
                my_list[j] = my_list[j - gap]
                j -= gap
            my_list[j] = current_item
        gap //= 2

    return my_list </pre>
###### test
<pre> assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
assert shell_sort([24, 22, 39, 34, 87, 73, 68]) == [22, 24, 34, 39, 68, 73, 87]
assert shell_sort([32, 30, 16, 96, 82, 83, 74]) == [16, 30, 32, 74, 82, 83, 96] </pre>
### 282
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to subtract two lists element-wise.

Your code should pass these tests:

assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
assert sub_list([1,2],[3,4])==[-2,-2]
assert sub_list([90,120],[50,70])==[40,50]

Your response should only contain the code for this function.

def sub_list(nums1,nums2):
    ...


 </pre>
###### answer
<pre> ```python
def sub_list(nums1, nums2):
    return [a - b for a, b in zip(nums1, nums2)]
``` </pre>
###### canonical_solution
<pre> def sub_list(nums1,nums2):
  result = map(lambda x, y: x - y, nums1, nums2)
  return list(result) </pre>
###### test
<pre> assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
assert sub_list([1,2],[3,4])==[-2,-2]
assert sub_list([90,120],[50,70])==[40,50] </pre>
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
<pre> ```python
def magic_square_test(my_matrix):
    n = len(my_matrix)
    
    # Calculate the sum of the first row to use as reference
    target_sum = sum(my_matrix[0])
    
    # Check rows
    for row in my_matrix:
        if sum(row) != target_sum:
            return False
            
    # Check columns
    for col in range(n):
        if sum(my_matrix[row][col] for row in range(n)) != target_sum:
            return False
            
    # Check main diagonal
    if sum(my_matrix[i][i] for i in range(n)) != target_sum:
        return False
        
    # Check secondary diagonal
    if sum(my_matrix[i][n-1-i] for i in range(n)) != target_sum:
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
### 117
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to convert all possible convertible elements in a list of lists to floats.

Your code should pass these tests:

assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
assert list_to_float( [("4", "4"), ("2", "27"), ("4.12", "9"), ("7", "11")] ) == [(4.0, 4.0), (2.0, 27.0), (4.12, 9.0), (7.0, 11.0)]
assert list_to_float( [("6", "78"), ("5", "26.45"), ("1.33", "4"), ("82", "13")] ) == [(6.0, 78.0), (5.0, 26.45), (1.33, 4.0), (82.0, 13.0)]

Your response should only contain the code for this function.

def list_to_float(test_list):
    ...


 </pre>
###### answer
<pre> ```python
def list_to_float(test_list):
    return [(float(a), float(b)) for a, b in test_list]
``` </pre>
###### canonical_solution
<pre> def list_to_float(test_list):
  res = []
  for tup in test_list:
    temp = []
    for ele in tup:
      if ele.isalpha():
        temp.append(ele)
      else:
        temp.append(float(ele))
    res.append((temp[0],temp[1])) 
  return res </pre>
###### test
<pre> assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
assert list_to_float( [("4", "4"), ("2", "27"), ("4.12", "9"), ("7", "11")] ) == [(4.0, 4.0), (2.0, 27.0), (4.12, 9.0), (7.0, 11.0)]
assert list_to_float( [("6", "78"), ("5", "26.45"), ("1.33", "4"), ("82", "13")] ) == [(6.0, 78.0), (5.0, 26.45), (1.33, 4.0), (82.0, 13.0)] </pre>
