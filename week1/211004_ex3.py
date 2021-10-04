import numpy as np

# 1. np.split(array, [i], axis=1): Numpy 배열 나누기
# array의 열에 해당하는 인덱스 i를 기준으로 나누기
array = np.arange(8).reshape(2, 4)
left, right = np.split(array, [2], axis=1)
print(left.shape)  # 형태를 출력
print(right.shape)
print(array)
print(left)
