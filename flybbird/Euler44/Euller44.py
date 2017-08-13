"""
오각수는 Pn = n (3n − 1)/2 라는 공식으로 구할 수 있고, 처음 10개의 오각수는 다음과 같습니다.
1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
위에서 P4 + P7 = 22 + 70 = 92 = P8이 됨을 볼 수 있습니다. 하지만 두 값의 차인 70 − 22 = 48 은 오각수가 아닙니다.
합과 차도 모두 오각수인 두 오각수 Pj, Pk 에 대해서, 그 차이 D = | Pk − Pj | 는 가장 작을 때 얼마입니까?
"""
import math

pentagonalData = []
index = 1
loop_value = True


# 오각수 만들기
def calc_pentagonal(num):
    return (num * ((3 * num) - 1)) / 2


# 오각수인지 확인하는 함수
# 똑똑한 재선님이 만들어 주신 함수
def check_pentagonal_number(val):
    return (math.sqrt((24 * val) + 1) + 1) % 6 == 0


while loop_value:
    # 오각수를 구해서 배열에 집어 넣기
    new_value = calc_pentagonal(index)
    pentagonalData.append(new_value)

    # 1개이상인 경우만
    if index > 1:
        for search_index in range(0, index - 1):
                first_value = pentagonalData[search_index]

                # 새로 추가된 값으로 매칭한다
                plus_value = first_value + new_value
                minus_value = new_value - first_value

                # 오각수인지를 체크한다.
                is_plus_number = check_pentagonal_number(plus_value)
                is_minus_number = check_pentagonal_number(minus_value)

                if (is_plus_number is True) and (is_minus_number is True):
                    print("===========================")
                    print("first_value = ", first_value)
                    print("second_value = ", new_value)
                    print("plus_value = ", plus_value)
                    print("minus_value = ", minus_value)
                    print("===========================")

                    loop_value = False
                    break

    index = index + 1
