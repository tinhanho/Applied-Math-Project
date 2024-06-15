from Image_Zoom_In import Linear_Way

def main():
    print("Choose Zoom In Method\n1: Linear")
    input_str = input()
    if input_str == '1':
        Linear_Way() # AKA Bilinear filtering

if __name__ == '__main__':
    main()
