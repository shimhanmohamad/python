def paintarea(test_h,test_w,cover):
    area =height * width
    paint_cane = round(area / coverage)
    print(f"To paint this wall we want {paint_cane} paint canes.")


height = int(input("Enter the height of the wall : "))
width = int(input("Enter the width of the wall :  "))
coverage = 5

paintarea(test_h=height,test_w=width,cover=coverage)
    