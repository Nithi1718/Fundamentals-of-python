# 1.  np.array()
# 2.  np.arange()
# 3.  np.linspace()
# 4.  np.zeros()
# 5.  np.ones()
# 6.  np.shape
# 7.  np.ndim
# 8.  np.size
# 9.  np.dtype
# 10. np.sum()
# 11. np.mean()
# 12. np.median()
# 13. np.min()
# 14. np.max()
# 15. np.std()
# 16. np.var()
# 17. np.percentile()
# 18. np.quantile()
# 19. np.where()
# 20. np.unique()
# 21. np.sort()
# 22. np.argsort()
# 23. np.argmax()
# 24. np.argmin()
# 25. np.reshape()
# 26. np.concatenate()
# 27. np.vstack()
# 28. np.hstack()
# 29. np.isnan()
# 30. np.nanmean()
# 31. np.nansum()
# 32. np.random.randint()
# 33. np.random.choice()
# 34. np.round()
# 35. np.sqrt()
# 36. np.abs()

import numpy as np

# a= np.array([[1,2,3,4],[4,5,6,7]])
# print(a)
# print(a.ndim)
# print(a.size)
# print(a.itemsize)
# print(a.dtype)
# print(a.shape)
#
#
# data = np.array([10, 20, 30, 40, 50, 60, 70])
#
# print(np.sum(data))
# print(np.mean(data))
# print(np.median(data))
# print(np.min(data))
# print(np.max(data))
# print(np.std(data))
# print(np.var(data))
# print(np.percentile(data, 80))


# data = np.array([[10, 20, 30],
#                  [40, 50, 60]])
#
# print(np.sum(data, axis=0))
# print(np.sum(data, axis=1))
# print(np.sum(data))

# np.mean(data, axis=0)
# np.mean(data, axis=1)
# np.max(data, axis=0)
# np.min(data, axis=1)





# data = np.array([10, 20, 30, 40, 50])
# print(data)

# data = np.arange(10,100)
# data = np.arange(10,110,10)
# print(data)

# data = np.linspace(0,100)
# data = np.linspace(0, 100, 6)
# print(data)

# data = np.zeros(5)
# data = np.zeros((2,5))
# print(data)

# data = np.ones(5)
# data = np.ones((2,5))
# print(data)

# data = np.full(5, 100)
# data = np.full((2,4), 100)
# print(data)

# data = np.eye(1)
# data = np.eye(2)
# data = np.eye(3)
# data = np.eye(4)
# data = np.eye(5)
# print(data)

# print(data.shape)
# print(data.ndim)
# print(data.size)
# print(data.dtype)

# sales = np.array([100, 200, 300, 400])
# print(np.sum(sales))
# print(np.max(sales))
# print(np.min(sales))
# print(np.mean(sales))
# print(np.median(sales))



# import numpy as np
#
# a = np.array([10, 20, 30])
# b = np.array([2, 4, 5])

# print(np.add(a, b))
# print(np.subtract(a, b))
# print(np.multiply(a, b))
# print(np.divide(a, b))
# print(np.power(a, 2))

# print(np.sqrt(b))
# print(np.abs(a))
# print(np.round(a,2))
# print(np.floor(a))
# print(np.ceil(a))

# data = np.array([10, 25, 30, 45, 50, 65])

# print(data[data > 30])
# print(data[data > 20])
# print(data[data < 50])
# print(data[data == 30])
# print(data[data != 30])
# print(data[(data > 20) & (data < 60)])
# print(data[(data > 20) | (data < 60)])

# data = np.array([10, 20, 30, 40, 50])
# print(np.where[data >= 30])
# print(np.where(data >= 30, "Pass", "Fail"))
# print(data.shape)

# data = np.array([1, 2, 3, 4, 5, 6])
# print(data.reshape(2, 3))
#
# a = np.array([[1, 2, 3],
#               [4, 5, 6]])
# print(a.flatten())
# print(a.ravel())


# a=np.array([1,2])
# b=a*2
# print(b)

a = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])
# print(a)
# print(a.reshape(1,20))
# print(a[1])
# print(a[0])
# print(a[0,::-1])
print(a[::-1])
print(np.sort(a[1,::-1]))


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints, marker = 'o',ls = 'dashed')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Super")
plt.show()