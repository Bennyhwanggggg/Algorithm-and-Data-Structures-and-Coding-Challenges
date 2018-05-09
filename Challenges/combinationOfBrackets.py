def validBrackets(output, op, cl, n):
    if op == n and cl == n:
        res.append(output)
        return
    else:
        if op < n:
            validBrackets(output+'(', op+1, cl, n)
        if cl < op:
            validBrackets(output+')', op, cl+1, n)


def allBrackets(n):
    validBrackets('', 0, 0, n)

res = []
allBrackets(3)
print(res)