
from Image_Zoom_In import Linear_Way
import pixel_replication
import test
image_path = 'PIL.jpg'
def main():
    print("Choose Zoom In Method\n1: Linear\n2: Pixel replication\n3: Bicubic\n4: All")
    input_str = input()
    if input_str == '1':
        Linear_Way(image_path) # AKA Bilinear filtering
    if input_str == '2':
        pixel_replication.pixel(image_path)
    if input_str == '3':
        test.bicubic(image_path)
    if input_str == '4':
        pixel_replication.pixel(image_path)
        Linear_Way(image_path)
        test.bicubic(image_path)

if __name__ == '__main__':
    main()
