import numpy as np

arr = np.arange(0,10,2)
# print(arr)

# height x width
zeroArr = np.zeros((10,5))
# print(zeroArr)

oneArr = np.ones((3,5))

# print(oneArr)

randomArr = np.random.randint(0,2000,100)
# print(randomArr)
newArr = randomArr.reshape((10,10))
# print(newArr[0,5])
# print(newArr)
print("\n\n\n\n")
newArr[0:3,0:3] = -1
print(newArr[0:3,0:3])
print(randomArr)
