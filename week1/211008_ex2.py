import cv2
import time

# 1. 이미지 크기 및 픽셀 확인
image = cv2.imread('book.jpg')
print(image.shape)  # 이미지 픽셀 수
print(image.size)  # 이미지 크기
px = image[100, 100]  # 이미지 객체의 특정 픽셀 가리키기
print(px)  # 이미지 객체를 출력하면 B, G, R 순서로 출력됨
print(px[2])  # R 값만 출력하기

# 2. 특정 범위 픽셀 변경
start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255, 255, 255]
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
image[0:100, 0:100] = [0, 0, 0]
print("--- %s seconds ---" % (time.time() - start_time))

cv2.imshow('Image', image)
cv2.waitKey(0)

# 3. ROI 추출 및 복사
# Numpy Slicing: ROI 처리 가능
logo = image[20:150, 70:200]
cv2.imshow('Image', logo)
cv2.waitKey(0)

# ROI 단위로 이미지 복사하기
image[0:130, 0:130] = logo
cv2.imshow('Image', image)
cv2.waitKey(0)

# 4. 픽셀별로 색상 다루기
image = cv2.imread('book.jpg')

# 특정 색상만 제거하기
image[:, :, 2] = 0
cv2.imshow('Image', image)
cv2.waitKey(0)
