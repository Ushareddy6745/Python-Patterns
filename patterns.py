# def pattern(rows):
#     for i in range(rows):
#         for j in range(i):
#             print(i, end=" ")
#         print()
# pattern(7)


# 1
def patterns(rows):
    for i in range(1,rows):
        for j in range(1,i+1):
            print(j,end=" ")
        print()  
    return
patterns(5)


# 2
    
def zero_one_triangle(rows):
    for i in range(1, rows):
        for j in range(1, i + 1):
            print((i +j+1) % 2, end=" ")
        print()
    return

zero_one_triangle(6)



# 3

def solidRhombus(rows):   
    for i in range(1, rows):
     
        for j in range(i):
            print(" ", end="")
     
        for j in range(rows):
            print("*", end="")
        print()
    return
solidRhombus(5)