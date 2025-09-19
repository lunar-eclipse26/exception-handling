try:
    age = int(input("please enter your age: "))
except ValueError:
    print("sir we need ur age not ur iq")
if age % 2 == 0:
    print("so ur age is an even number")
else:
    print("ok ur age is an odd number")
