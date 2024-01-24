A = int(input())
B = int(input())
if A <= B:
    if A % 2 == 0:
            for i in range(A + 2,B,2):
                print(i, end = " ")
    else:
        for i in range(A+1,B,2):
            print(i, end = " ")