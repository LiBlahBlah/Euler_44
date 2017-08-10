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
