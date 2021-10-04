import numpy as np

# 1. 배열 합치기 np.concatenate([arr1, arr2])
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.concatenate([array1, array2])  # 배열 합치기

print(array3.shape)  # .shape: 크기
print(array3)

# 2. 배열 형태 바꾸기(1차원 -> 2차원) array.reshape(a, b)
# a x b의 배열 생성
array4 = np.array([1, 2, 3, 4])
array5 = array4.reshape(2, 2)
print(array5)

# 3. Numpy 배열 세로 축으로 합치기
# 열이 같을 때: axis=0 (세로로 합치기)
# 행이 같을 때: axis=1 (가로로 합치기)
array6 = np.arange(4).reshape(1, 4)
array7 = np.arange(8).reshape(2, 4)
print(array6)
print(array7)

array8 = np.concatenate([array6, array7], axis=0)
print(array8)

