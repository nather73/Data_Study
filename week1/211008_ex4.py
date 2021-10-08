import cv2

# 이미지 합치기 방법
# 1) cv2.add(): Saturation 연산 수행, 0보다 작으면 0, 255보다 크면 255로 표현
# 2) np.add(): Modulo 연산 수행, 256은 0, 257은 1로 표현
image_1 = cv2.imread('book.jpg')
image_2 = cv2.imread('book.jpg')
image_1[:, :, 0] = 0
image_2[:, :, 2] = 0

result = cv2.add(image_1, image_2)
cv2.imshow('Image', result)
cv2.waitKey(0)

result = image_1 + image_2
cv2.imshow('Image', result)
cv2.waitKey(0)
