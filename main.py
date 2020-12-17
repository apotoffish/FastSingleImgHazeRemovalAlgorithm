import imutils as imutils
from cv2 import cv2
import gaussian_noise as gs

img_path=("origin_pic/")
tgt_path=("target/")
bgr_img=cv2.imread(img_path+"1.jpg",1)

noise_img=gs.gasuss_noise(bgr_img)
resized_img=cv2.resize(noise_img,(600,450))

cv2.imshow('noise image', imutils.resize(bgr_img,600,450))  #利用imutils模块调整显示图像大小
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

cv2.imwrite(tgt_path+'noise_005_img1.jpg',resized_img)