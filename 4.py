def quay_lui(n, s):
    if n == 1: 
        return s
    else:
        result = []
        for digit in quay_lui(1, s):
            for bits in quay_lui(n-1, s):
                result.append(digit + bits)
        return result

print(quay_lui(3,"01"))