import numpy as np

# 1. numpy data
list_data = [1, 2, 3]
array = np.array(list_data)

print(array)
print(array.size)   # .size
print(array.dtype)  # data type
print(array[2])     # index 접근이 가능하다!

# 2. np.arange(n): 0 이상 n 이하까지 배열 생성
array1 = np.arange(4)
print(array1)

# 3. np.zeros((a, b), dtype=<type>)
# a x b 배열 생성, 값은 0으로 초기화, date type은 <type>
array2 = np.zeros((4, 4), dtype=float)
print(array2)
array3 = np.ones((3, 4), dtype=str)
print(array3)

# 4. np.random.randint(x, y, (a, b)): 랜덤한 값으로 배열 초기화하기
# 0 이상 10 이하의 random value, a x b 배열 생성
array4 = np.random.randint(0, 10, (3, 3))
print(array4)

# 5. np.random.normal(x, y, (a, b))
# 평균이 x이고 표준편차가 y인 표준정규를 띠는 a x b 배열 생성
array5 = np.random.normal(0, 1, (3, 3))
print(array5)
