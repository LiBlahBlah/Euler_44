import math

# 오각수 공식
def calculate(n):
    return (n*((3*n)-1))/2

# 오각수 공식 Pn = ( n * ( ( 3 * n ) - 1 ) ) / 2
# 근의 공식 n = ( 1 + math.sqrt( ( 24 * Pn ) + 1 ) ) / 6
# Pn을 대입하여 n이 정수인지 확인한다. 정수면 오각수.
def isPentagonalNumber(value) :
    return (math.sqrt((24*value)+1) + 1 ) % 6 == 0

loop = True
k = 2
while loop :
    for j in range(1, k) :
        c1 = calculate(j)
        c2 = calculate(k)
        r1 = c2 - c1
        r2 = c2 + c1
        b1 = isPentagonalNumber(r1) #Pk+Pj가 오각수인지 확인
        b2 = isPentagonalNumber(r2) #Pk-Pj가 오각수인지 확인

        if (b1 and b2) :
            print("======")
            print("result = ",r1)
            print("======")
            loop = False

    k = k+1