#broadcasting means that numpy will automatically expand the smaller array to match the shape of the larger array during arithmetic operations.#
# In this case, the scalar values (5, 2, and 10) are broadcasted to match the shape of the array 'a', allowing for element-wise operations.

import numpy as np
a=np.array([10,20,30])

#print(a+5) # each eleement of the array is added by 5
#print(a*2) # each element of the array is multiplied by 2
#print(a/10) # each element of the array is divided by 10

print(a.reshape(3,1)) # reshape array a into a col with 3 rows n 1 column
# [[10]
#  [20]
#  [30]]

print(a.reshape(3,1) + np.array([0,1,2])) # reshaping the array 'a' to a column vector and adding it to a row vector, resulting in a 3x3 matrix
 #here the new array is a plain 1-D array so it need to match the reshpaed array 'a
# so a = (3,1) - 3 rows, 1 col
# [0,1,2] = is (3,) which is small than a, so need to match it to 2-d hence numpy change it to (1,3) - 1 row, 3 col
# [[10]
#  [20]    +  [0,1,2]
#  [30]]
#[10 11 12]
# [20 21 22]
# [30 31 32]]
print(a.shape)

