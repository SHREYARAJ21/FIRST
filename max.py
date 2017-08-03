print("enter the values")
x=raw_input("first value")
y=raw_input("second value")
z=raw_input("third value")
def max_of_three(x,y,z):
    Max = x
    if y > Max:
        Max = y
    if z > Max:
        Max =z
    return Max
print("the largest value:")
print x