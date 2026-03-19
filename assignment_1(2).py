
def rectangle(l, w):
    return l * w, 2 * (l + w)             # (area, perimeter)
    
length = float(input("Length: "))
width  = float(input("Width: "))
area, peri = rectangle(length, width)

print(f"Area = {area}, Perimeter = {peri}")