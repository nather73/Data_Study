import numpy as np

# 1. Numpy 원소의 정렬
array = np.array([5, 9, 10, 3, 1])
array.sort()
print(array)  # 오름차순
print(array[::-1])  # 내림차순

# 2. 각 열을 기준으로(행을 따라) 정렬: .sort(axis=0)
array1 = np.array([[5, 9, 10, 3, 1], [8, 3, 4, 2, 5]])
print(array1)
array1.sort(axis=0)
print(array1)

# 3. 균일한 간격으로 데이터 생성
# np.linspace(a, b, x): a부터 b 사이의 데이터 x개를 채움
array2 = np.linspace(0, 10, 5)
print(array2)  # 임의의 데이터셋을 만들고자 할 때 자주 사용됨

# 4. 난수의 재연 (seed: 실행마다 결과 동일)
# 이후 다양한 머신러닝 기법을 실습할 때 사용함.
np.random.seed(7)
print(np.random.randint(0, 10, (2, 3)))

# 5. Numpy 배열 객체 복사
# Numpy의 경우 내부적으로 array3과 array4가 동일한 주소를 가리킴.
array3 = np.arange(0, 10)
array4 = array3
array4[0] = 99
print(array3)  # Error!
array5 = np.arange(0, 10)
array6 = array5.copy()
array6[0] = 99
print(array5)  # Correct!

# 6. 중복된 원소 제거하기: np.unique(arr)
array7 = np.array([1, 1, 2, 2, 2, 3, 3, 4])
print(np.unique(array7))
