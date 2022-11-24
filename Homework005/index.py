import numpy as np



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
  today = np.datetime64('today', 'D')
  yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
  tomorrow =np.datetime64('today', 'D') + np.timedelta64(1, 'D')
  print(today)
  print(yesterday)
  print(tomorrow)


def task5():
  arr = np.random.uniform(low=0.5, high=13.3, size=(5,))
  

def main():
  # task1()
  # task2()
  # task3()
  # task4()
  task5()


if __name__ == "__main__":
    main()
