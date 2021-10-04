import numpy as np

# 1. Numpy의 기본 연산

array = np.random.randint(1, 10, size=4).reshape(2, 2)
print(array)

result_array = array * 10
print(result_array)

# 2. 서로 다른 형태의 Numpy 연산
# 배열의 연산은 행 우선으로 실행된다.
array1 = np.arange(4).reshape(2, 2)  # (2 x 2)
array2 = np.arange(2)  # (1 x 2)
array3 = array1 + array2
print(array3)

# 3. 브로드캐스트: 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환
array4 = np.arange(0, 8).reshape(2, 4)
array5 = np.arange(0, 8).reshape(2, 4)
array6 = np.concatenate([array4, array5], axis=0)
array7 = np.arange(0, 4).reshape(4, 1)

print(array6)
print(array7)
print(array6 + array7)

# 4. Numpy의 마스킹 연산
# 마스킹: 각 원소에 대하여 조건을 만족하는지 체크

array8 = np.arange(16).reshape(4, 4)
print(array8)

array9 = array8 < 10
print(array9)

# 마스킹 연산이 수행된 배열을 넣게 되면 그 조건을 만족하는 데이터만 특정 작업을 수행하겠다고 명시할 수 있다.
array8[array9] = 100
print(array8)
# 일일이 원소 하나를 방문해서 조건을 처리하지 않아도 됨.

# 5. Numpy의 집계 함수
arr = np.arange(16).reshape(4, 4)
print("최댓값: ", np.max(arr))
print("최솟값: ", np.min(arr))
print("합계: ", np.sum(arr))
print("평균값: ", np.mean(arr))

# 6. 특정한 축을 기준으로 집계 함수 수행하기
# axis=0은 행을 따라 계산, axis=1은 열을 따라 계산
print(arr)
print("합계: ", np.sum(arr, axis=0))
print("합계: ", np.sum(arr, axis=1))
