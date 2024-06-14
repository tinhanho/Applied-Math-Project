from Image_Zoom_In import Cubic_Spline_Way, Linear_Way, Mixed_Way

def main():
    print("Choose Zoom In Method\n1: Linear 2: Cubic Spline 3: Mixed")
    input_str = input()
    if input_str == '1':
        Linear_Way() # AKA Bilinear filtering
    elif input_str == '2':
        Cubic_Spline_Way() # TODO: Use bicubic interpolation over 4x4 pixel neighborhood
    elif input_str == '3':
        Mixed_Way() # TODO: Use 4x4 as well

if __name__ == '__main__':
    main()
