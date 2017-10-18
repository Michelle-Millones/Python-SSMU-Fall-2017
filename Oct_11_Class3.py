def fizzbuzz(x):
    if x%5 == 0 and x%3 == 0:
        print("fizzbuzz")
    elif x%3 == 0:
        print("fizz")
    elif x%5 == 0:
        print("buzz")

def grade_me(x):
    if x>=85:
        print("A")
    elif x>=80 and x<84:
        print("A-")
    elif x>=75 and x<79:
        print("B+")
    elif x>=70 and x<74:
        print("B")
    elif x>=65 and x<69:
        print("B-")
    elif x>=60 and x<64:
        print("C+")
    elif x>=55 and x<59:
        print("C")
    elif x>=50 and x<54:
        print("D")
    else:
        print("F")
