import numpy as np

x = np.array([12,33])
print(x)
print(type(x))
print(np.__version__)

list1 = [[1,2,3],[11,22,33]]
list2 = [[4,5,6],[44,55,66]]
list3 = [[7,8,9],[77,88,99]]

arr = np.array([list1, list2, list3])
print(arr)
print(arr.ndim)
# print(type(arr))

print("Shape",arr.shape)
print("Size",arr.size)
print("Dtype",arr.dtype)


l1 = [1,3,5,7,9]

arr2 = np.array(l1)

print("Shape",arr2.shape) #5,
print("Size",arr2.size) #5
print("Dtype",arr2.dtype) #int64
print("Ndim",arr2.ndim) #1

#Zero array and ones array

zero_array = np.zeros((2,3))
ones_array = np.ones((2,3))
print(zero_array)
print(ones_array)

full_array = np.full((3,2), 7)
print(full_array)

# identity matrix

ide_array = np.identity((5))
print(ide_array)

# empty array

empty_array = np.empty((2))
print(empty_array)

# arrange array 

array = np.arange(1,11,1)
print(array)

# make the exact parts

array = np.linspace(1,10,4)
array2 = np.linspace(1,10,10)
print(array)
print(array2)

# Random numbers array 

rint_arr = np.random.randint(1,100,(3,3))
print(rint_arr)

a = np.array([1,3,5,7,9])
print(a[:3])

b = np.array([1,2,3,4,5,6,7,8,9,10])
print(b[::2])

c = np.array([[1,2,3],[4,5,6]])
print(c[1][1])
print(c[:, 2])

d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(d)
print(d[1:,2])
print(d[1:,1])
print(d[1,1:])

# Reshaping 

array = np.array([1,2,3,4,5,6])
print(array.reshape(2,3))
print(array.reshape(6,1))

# flatten

array = np.array([[1,2,3],[4,5,6]])
print(array.flatten())

array = np.arange(1,26,1)
array2 = array.reshape(5,5)
print(array2)
print(array2[-1])
print(array2[:,0])
print(array2[:3,:3])

array = np.array([1,2,3])
print(array.reshape(3,1)*array)
