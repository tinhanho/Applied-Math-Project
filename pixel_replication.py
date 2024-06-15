import cv2
import numpy as np

def pixel_replication_zoom(image):
    height, width, channels = image.shape
    new_width = width * 2
    new_height = height * 2
    
    # 創建一個新的圖片尺寸
    new_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)
    
    # 像素複製放大
    for h in range(new_height):
        for w in range(new_width):
            for c in range(channels):
                if( h%2 == 0):
                    if( w%2 == 0):
                        new_image[h][w][c] = image[h//2][w//2][c]
                    else:
                        new_image[h][w][c] = new_image[h][w-1][c]
                else:
                    if( w%2 == 0):
                        new_image[h][w][c] = new_image[h-1][w][c]
                    else:
                        new_image[h][w][c] = new_image[h][w-1][c]
    
    # 保存放大後的圖片
    cv2.imwrite('pixel_replication.jpg', new_image)


image_path = 'Applied-Math-Project-main\PIL.jpg'
image = cv2.imread(image_path)
pixel_replication_zoom(image)

