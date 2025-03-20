# mbpp / ruadapt-qwen-32b
### 63
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the maximum difference between available pairs in the given tuple list.

Your code should pass these tests:

assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23

Your response should only contain the code for this function.

def max_difference(test_list):
    ...


 </pre>
###### answer
<pre> def max_difference(test_list):
    # Calculate the difference for each tuple and find the maximum
    max_diff = max([abs(pair[1] - pair[0]) for pair in test_list])
    return max_diff

# These assert statements are used to validate the solution
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23 </pre>
###### canonical_solution
<pre> def max_difference(test_list):
  temp = [abs(b - a) for a, b in test_list]
  res = max(temp)
  return (res)  </pre>
###### test
<pre> assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23 </pre>
### 59
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the nth octagonal number.

Your code should pass these tests:

assert is_octagonal(5) == 65
assert is_octagonal(10) == 280
assert is_octagonal(15) == 645

Your response should only contain the code for this function.

def is_octagonal(n): 
    ...


 </pre>
###### answer
<pre> def is_octagonal(n): 
    # Formula to calculate the nth octagonal number
    return n*(3*n - 2)

# The provided test cases can be validated using the function as follows:
# assert is_octagonal(5) == 65
# assert is_octagonal(10) == 280
# assert is_octagonal(15) == 645 </pre>
###### canonical_solution
<pre> def is_octagonal(n): 
	return 3 * n * n - 2 * n  </pre>
###### test
<pre> assert is_octagonal(5) == 65
assert is_octagonal(10) == 280
assert is_octagonal(15) == 645 </pre>
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
<pre> import cmath

def convert(numbers):
    # Convert the number to a complex number
    complex_num = complex(numbers)
    # Convert to polar coordinates
    polar_coordinates = cmath.polar(complex_num)
    return polar_coordinates </pre>
###### canonical_solution
<pre> import cmath  
def convert(numbers):    
  num = cmath.polar(numbers)  
  return (num)  </pre>
###### test
<pre> assert convert(1) == (1.0, 0.0)
assert convert(4) == (4.0,0.0)
assert convert(5) == (5.0,0.0) </pre>
### 419
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.

Your code should pass these tests:

assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
assert round_and_sum([5,2,9,24.3,29])==345
assert round_and_sum([25.0,56.7,89.2])==513

Your response should only contain the code for this function.

def round_and_sum(list1):
    ...


 </pre>
###### answer
<pre> def round_and_sum(list1):
    rounded_list = [round(num) for num in list1]
    sum_of_elements = sum(rounded_list)
    total = sum_of_elements * len(list1)
    print(total)
    return total

# Test cases
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]) == 243
assert round_and_sum([5,2,9,24.3,29]) == 345
assert round_and_sum([25.0,56.7,89.2]) == 513 </pre>
###### canonical_solution
<pre> def round_and_sum(list1):
  lenght=len(list1)
  round_and_sum=sum(list(map(round,list1))* lenght)
  return round_and_sum </pre>
###### test
<pre> assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
assert round_and_sum([5,2,9,24.3,29])==345
assert round_and_sum([25.0,56.7,89.2])==513 </pre>
### 412
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to remove odd numbers from a given list.

Your code should pass these tests:

assert remove_odd([1,2,3]) == [2]
assert remove_odd([2,4,6]) == [2,4,6]
assert remove_odd([10,20,3]) == [10,20]

Your response should only contain the code for this function.

def remove_odd(l):
    ...


 </pre>
###### answer
<pre> def remove_odd(l):
    return [num for num in l if num % 2 == 0]

 </pre>
###### canonical_solution
<pre> def remove_odd(l):
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return l </pre>
###### test
<pre> assert remove_odd([1,2,3]) == [2]
assert remove_odd([2,4,6]) == [2,4,6]
assert remove_odd([10,20,3]) == [10,20] </pre>
### 93
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to calculate the value of 'a' to the power 'b'.

Your code should pass these tests:

assert power(3,4) == 81
assert power(2,3) == 8
assert power(5,5) == 3125

Your response should only contain the code for this function.

def power(a,b):
    ...


 </pre>
###### answer
<pre> def power(a,b):
    return a ** b </pre>
###### canonical_solution
<pre> def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1) </pre>
###### test
<pre> assert power(3,4) == 81
assert power(2,3) == 8
assert power(5,5) == 3125 </pre>
### 250
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.

Your code should pass these tests:

assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 3
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 4

Your response should only contain the code for this function.

def count_X(tup, x): 
    ...


 </pre>
###### answer
<pre> def count_X(tup, x): 
    return tup.count(x)

 </pre>
###### canonical_solution
<pre> def count_X(tup, x): 
    count = 0
    for ele in tup: 
        if (ele == x): 
            count = count + 1
    return count  </pre>
###### test
<pre> assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 3
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 4 </pre>
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
<pre> def sum_div(number):
    result = 0
    for i in range(1, number):
        if number % i == 0:
            result += i
    return result
 </pre>
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
### 433
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to check whether the entered number is greater than the elements of the given array.

Your code should pass these tests:

assert check_greater([1, 2, 3, 4, 5], 4) == False
assert check_greater([2, 3, 4, 5, 6], 8) == True
assert check_greater([9, 7, 4, 8, 6, 1], 11) == True

Your response should only contain the code for this function.

def check_greater(arr, number):
    ...


 </pre>
###### answer
<pre> def check_greater(arr, number):
    return all(number > x for x in arr)

# Test cases to validate the solution
assert check_greater([1, 2, 3, 4, 5], 4) == False
assert check_greater([2, 3, 4, 5, 6], 8) == True
assert check_greater([9, 7, 4, 8, 6, 1], 11) == True </pre>
###### canonical_solution
<pre> def check_greater(arr, number):
  arr.sort()
  return number > arr[-1] </pre>
###### test
<pre> assert check_greater([1, 2, 3, 4, 5], 4) == False
assert check_greater([2, 3, 4, 5, 6], 8) == True
assert check_greater([9, 7, 4, 8, 6, 1], 11) == True </pre>
### 458
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the area of a rectangle.

Your code should pass these tests:

assert rectangle_area(10,20)==200
assert rectangle_area(10,5)==50
assert rectangle_area(4,2)==8

Your response should only contain the code for this function.

def rectangle_area(l,b):
    ...


 </pre>
###### answer
<pre> def rectangle_area(l,b):
    return l * b </pre>
###### canonical_solution
<pre> def rectangle_area(l,b):
  area=l*b
  return area </pre>
###### test
<pre> assert rectangle_area(10,20)==200
assert rectangle_area(10,5)==50
assert rectangle_area(4,2)==8 </pre>
