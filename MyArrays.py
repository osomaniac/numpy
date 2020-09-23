import numpy as np


# 1D Array
'''
integers = np.array([1,2,3])
print(integers)
'''


# 2D Array
integers = np.array([[1,2,3],[4,5,6]])
'''
print(integers.dtype) # tells us what type of values are stored in the array
print(integers.ndim) # tells us how many dimensions there are in the array
print(integers.shape) # tells us the shape (rows, columns) of the array
print(integers.size) # give total number of elements in array
print(integers.itemsize) # gives memory size taken up by array
'''
for row in integers:
    print(row)
    print()

    for col in row:
        print(col, end=' ')
    print()


for i in integers.flat: # goes through all of the elemets in an array ignoring rows/columns
    print(i, end=" ")


print()
print(np.zeros(5)) # creates an array of 5 zeros
print(np.ones(5)) # creates an array of 5 ones
print()
print()


array1 = np.ones((2,4), dtype=int) # arrays default to floats so we use dtype to define what type we want
print(array1)
print()


array2 = np.full((3,5), 13, dtype=int) # creates a 3x5 array of the number 13
print(array2)
print()


print(np.arange(5)) #creates an array containing five objects starting at 0 ([0,1,2,3,4])
print(np.arange(5,10)) # starts at 5 goes all the way to 9
print(np.arange(10,1,-2)) # starts at 10 and goes down by 2 to 2
print(np.linspace(0.0,1.0,num=5)) # gives array of 5 evenly spaced numbers between 0 and 1 (limits included)
print()


array1 = np.arange(1,21) # creats a 1D array with 20 elements
print(array1)
array2 = array1.reshape(4,5) # splits the 1D array into a 4x5 array, have to provide exact amount of spaces or it errors
print(array2)


array3 = np.arange(1,100001).reshape(4,25000)
print(array3) # large arrays are printed without middle columns, you see first and last three of each row

array4 = np.arange(1,100001).reshape(100,1000)
print(array4) # large arrays are printed without middle rows, you see first and last three of column


numbers = np.arange(1,6)
numbers *= 2 # multiples all variables in array by 2
print(numbers) 

print(numbers + 10) # adds 10 to each variable in the array

print(numbers ** 3) # numbers^3, exponent

print(numbers >= 13) # gives you a new array of the result for each element compared to 13


numbers2 = np.arange(5,10)
print(numbers)
print(numbers2)
print(numbers2 > numbers) # gives you a new array of the result for each element compared to the other
print(numbers == numbers2) 