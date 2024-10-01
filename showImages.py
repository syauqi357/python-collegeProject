import cv2

path = r'G:\01 - KULIAH\SEMESTER 5\01-PENGOLAHAN CITRA\tugas1\anyaForger.jpeg'

image = cv2.imread(path, 0)

windows_name = 'image'

cv2.imshow(windows_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()