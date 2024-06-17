
from Image_Zoom_In import Linear_Way
import pixel_replication
import test
def main():
    print("Choose Zoom In Method\n1: Linear\n2: Pixel replication\n3: Bicubic")
    input_str = input()
    if input_str == '1':
        Linear_Way() # AKA Bilinear filtering
    if input_str == '2':
        pixel_replication.pixel()
    if input_str == '3':
        test.bicubic()

if __name__ == '__main__':
    main()
