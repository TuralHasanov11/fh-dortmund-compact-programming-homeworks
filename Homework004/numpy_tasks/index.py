import numpy as np
import matplotlib.pyplot as plt


def task1():
  vector = np.arange(10, 50)
  print(vector)
  vector = np.flip(vector)
  print(vector)


def task2():
  arr = np.random.rand(5,5)
  print(arr)
  minVal = np.amin(arr)
  print(minVal)
  maxVal = np.amax(arr)
  print(maxVal)


def task3():
  matrix = np.arange(25).reshape(5, 5) 
  print(matrix)
  row_sums = matrix.sum(axis=1)
  new_matrix = matrix / row_sums[:, np.newaxis]
  print(new_matrix)


def task4():
  matrix1 = np.arange(15).reshape(5, 3) 
  print(matrix1)
  matrix2 = np.arange(6).reshape(3, 2) 
  print(matrix2)
  product = np.dot(matrix1, matrix2)
  print(product)
  

def task5():
  today = np.datetime64('today', 'D')
  yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
  tomorrow =np.datetime64('today', 'D') + np.timedelta64(1, 'D')
  print(today)
  print(yesterday)
  print(tomorrow)


def task6():
  arr = np.random.uniform(low=0.5, high=13.3, size=(5,))
  print(arr)
  # Method 1
  print(arr.astype(int))
  # Method 2
  print(np.int_(arr))
  # Method 3
  print(np.array([int(a) for a in arr]))
  # Method 4
  print(np.array(list(map(int, arr))))
  # Method 5
  print(np.array(arr, int))
  plt.pie(arr, labels=["Number 1", "Number 2", "Number 3", "Number 4", "Number 5"], shadow = True)
  plt.show()
  
  

def task7():
  arr = np.array([np.array([np.random.randint(0, high=20, size=2, dtype=int), np.random.randint(0, high=255, size=3, dtype=int)]) for x in range(1,10)])
  print(arr)
  

def integerGenerator():
  pass

def task8():
  pass


def task9():
  arr1 = np.random.rand(10)
  arr2 = np.random.rand(10)
  print(arr1)
  print(arr2)
  if np.array_equal(arr1, arr2):
    print("Equal")
  else:
    print("Not equal")


def task10():
  a = np.random.random((100,2))
  x,y = np.atleast_2d(a[:,0], a[:,1])
  d = np.sqrt( (x-x.T)**2 + (y-y.T)**2)
  print(d)


def task11():
  a = np.random.rand(3, 4)
  print(a)
  b = a - a.mean(axis=1, keepdims=True)
  print(b)
  

def task12():
  a = np.random.random((3,3)) * 10
  print(a)
  column = 1 # sort by column
  a = a[a[:,column].argsort()] 
  print(a)


def task13():
  matrix = np.arange(16).reshape(4, 4)
  print(matrix)
  rank = np.linalg.matrix_rank(matrix)
  print(rank)
  
  
def task14():
  array = np.arange(256).reshape(16, 16)
  print(array)
  blockSize = 4
  blockSum = np.add.reduceat(np.add.reduceat(array, np.arange(0, array.shape[0], blockSize), axis=0), 
                            np.arange(0, array.shape[1], blockSize), axis=1)
  print(blockSum)




def main():
  # task1()
  # task2()
  # task3()
  # task4()
  # task5()
  task6()
  # task7()
  # task8()
  # task9()
  # task10()
  # task11()
  # task12()
  # task13()
  # task14()

if __name__ == "__main__":
    main()
