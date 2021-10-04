import numpy as np

# 1. 단일 객체 저장 및 불러오기
array = np.arange(0, 10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result)

# 2. 복수 객체 저장 및 불러오기
# 복수 객체가 담겨 있을 경우, 불러온 다음 저장했을 때 사용했던 객체 이름 인덱스로 데이터를 불러올 수 있다.
array1 = np.arange(0, 10)
array2 = np.arange(10, 20)
np.savez('saved.npz', arr1=array1, arr2=array2)

data = np.load('saved.npz')
result1 = data['arr1']
result2 = data['arr2']
print(result1)
print(result2)
