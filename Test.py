import cv2
import numpy as np


def compare_images_pixel():
    image_path1 = "1.png"  # 第一张图片的路径
    image_path2 = "2.png"  # 第二张图片的路径
    # 读取两张图片
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)
    x, y, w, h = 50, 50, 100, 100

    # 提取左上角区域
    img1 = img1[y:y+h, x:x+w]
    img2 = img2[y:y+h, x:x+w]
    # 计算每个像素通道的颜色值差异
    diff_image = cv2.absdiff(img1, img2)
    diff_pixels = np.sum(diff_image, axis=2)  # 计算通道差异总和
    different_pixel_count = np.count_nonzero(diff_pixels)
    print(different_pixel_count)


compare_images_pixel()


# different_pixel_count = compare_images_pixel(image_path1, image_path2)
# print(f"不同像素的数量：{different_pixel_count}")
