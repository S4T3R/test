a = int(input("dien 1 so: "))
b = int(input("dien 1 so: "))
def UCLN(a,b):
        if a <= b:
            if b % a == 0:
                return a
            c = b - a
            while c > 0:
                b = b - c
                a = b - (a - c)
                d = a
                c = b - a
            if c < 0:
                return 1
            return a,b,c,d
            
            
        
        elif a >= b :
            if a % b == 0:
                return b
            c = a - b
            while c > 0:
                a = a - c
                b = a - (b - c)
                d = a
                c = a - b
            if c < 0:
                return 1
            return d


print("uoc chung lon nhat la: ", UCLN(7,6))


def min(a,b):
    ucln = UCLN(a,b)
    c = a/ucln
    d = b/ucln

    return c

def mix(a,b):
    ucln = UCLN(a,b)
    c = a/ucln
    d = b/ucln

    return d


print(min(a,b), "/", mix(a,b))