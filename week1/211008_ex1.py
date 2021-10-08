import cv2

# 1. 이미지 읽어서 살펴보기
# cv2.imread(file_name, flag): 이미지를 읽어 Numpy 객체로 만드는 함수
# 반환 값: Numpy 객체(행, 열, 색상: 기본 BGR)
# cv2.imshow(title, image): 특정한 이미지를 화면에 출력함
# cv2.imwrite(file_name, image): 처리가 끝난 이미지를 파일로 저장하는 함수
# cv2.waitKey(time): OpenCV 윈도우 창에서 키보드 입력을 처리하는 함수
# cv2.destroyAllWindows(): 화면의 모든 윈도우를 닫는 함수

img_basic = cv2.imread('book.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Image Basic', img_basic)
cv2.waitKey(0)
cv2.imwrite('result1.png', img_basic)

cv2.destroyAllWindows()

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Gray', img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png', img_gray)
