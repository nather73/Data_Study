import cv2
import numpy as np

# 1. 이미지 크기 조절
# cv2.resize(image, dsize, fx, fy, interpolation)
# dsize: Manual Size, fx: 가로 비율, fy: 세로 비율
# INTER_CUBIC: 사이즈를 크게 할 때, INTER_AREA: 사이즈를 작게 할 때
image = cv2.imread('book.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)

expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Image', expand)
cv2.waitKey(0)

shrink = cv2.resize(image, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
cv2.imshow('Image', shrink)
cv2.waitKey(0)

# 2. 이미지 위치 변경
# cv2.warpAffine(image, M, dsize), M: 변환 행렬
height, width = shrink.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 10]])
dst = cv2.warpAffine(shrink, M, (width, height))
cv2.imshow('Image', dst)
cv2.waitKey(0)

# 3. 이미지 회전
# cv2.getRotationMatrix2D(center, angle, scale): 이미지 회전을 위한 변환 행렬 생성
# center: 회전 중심, angle: 회전 각도, scale: Scale Factor
height, width = image.shape[:2]
M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Image', dst)
cv2.waitKey(0)
