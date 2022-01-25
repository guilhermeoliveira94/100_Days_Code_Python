import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height, wight, cover):
    num_cans = ((height*wight)/cover)
    print(f"You'll need {int(math.ceil(num_cans))} cans of paint.")


paint_calc(height=test_h, wight=test_w, cover=coverage)