# Euler 44 풀이

## 무식하게 돌자
- 계산(합,차) 결과가 오각수인지 판단은 역함수를 이용한다
- [함수 그래프 보기](https://www.wolframalpha.com/input/?i=y%3Dx(3*x-1)%2F2)
- [역함수 구하기](https://www.wolframalpha.com/input/?i=inverse+function+of+y%3Dx(3*x-1)%2F2)
- 최소값은 최초로 나온 값이다 (∵ 발산하는 함수니까)
- 1~3000 번까지 무식하게 돌면서 찾기 (∵ 2,500번대에서 최초 값이 나오더라)
- 값의 범위가 주어지지 않았기 때문에 첫번째 값이 나올 때 까지 찾아야 한다 <br/>
  그런데 두개의 값을 사용해야 해서 2중 루프롤 돌려고 하니까 범위를 제한하고 돌아야 하기 때문에 <br/>
  그냥 임의의 값(3000)을 사용했음

## 소스코드
```python
import math

# https://www.wolframalpha.com/input/?i=y%3Dx(3*x-1)%2F2
penta = lambda n: int(n * (3 * n - 1) / 2)

# https://www.wolframalpha.com/input/?i=inverse+function+of+y%3Dx(3*x-1)%2F2
inversePenta = lambda pn: int((1 + math.sqrt(24 * pn + 1)) / 6)

isPenta = lambda pn: penta(inversePenta(pn)) == pn

loopTo = 3000
for i in range(1, loopTo):
    for j in range(i + 1, loopTo):
        pi = penta(i)
        pj = penta(j)
        sum = pi + pj
        sub = abs(pi - pj)
        if isPenta(sum) and isPenta(sub):
            print("P{} + P{} = P{} ({})".format(i, j, inversePenta(sum), sum))
            print("P{} - P{} = P{} ({})".format(i, j, inversePenta(sub), sub))
```

## Result
- 대략 11초 정도 걸림
```python
P1020 + P2167 = P2395 (8602840)
P1020 - P2167 = P1912 (5482660)
```