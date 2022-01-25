import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height, wigth, cover,num_cans):
    num_cans = ((height*wigth)/cover)
    print(int(math.ceil(num_cans)))


paint_calc(height=test_h, width=test_w, cover=coverage, num_cans = 0)