# 1-qadam
def hello():
    return "Hello, World!"

def kvadrat(a):
    return a * a

def kub(a):
    return a ** 3

# 2-qadam arifmetik amallar

def yigindi(a, b):
    return a + b

def ayirma(a, b):
    return a - b

def kopaytma(a, b):
    return a * b

def bolish(a, b):
    if b == 0:
        return "Xato: 0 ga bo'lish mumkin emas!"
    return a / b

# 3-qadam. taqqoslash funksiyalari

def max_son(a, b):
    if a >= b:
        return a
    return b

def min_son(a, b):
    if a <= b:
        return a
    return b

def juftmi(a):
    if a % 2 == 0:
        return True
    return False

def toqmi(a):
    if a % 2 != 0:
        return True
    return False

# 4-qadam. string funksiyalarini qoshish

def katta_harf(matn):
    return matn.upper()

def kichik_harf(matn):
    return matn.lower()

def teskari(matn):
    return matn[::-1]

def uzunligi(matn):
    return len(matn)

# 5-qadam. list funksiyalari qoshildi

def yigindi_list(lst):
    yig = 0
    for i in lst:
        yig += i
    return yig

def eng_katta(lst):
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

def eng_kichik(lst):
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

def uzunligi_list(lst):
    return len(lst)

# 6-qadam. matematik funksiyalar qoshildi

def faktorial(n):
    natija = 1
    for i in range(1, n + 1):
        natija *= i
    return natija

def daraja(a, b):
    return a ** b

def abs_son(a):
    if a < 0:
        return -a
    return a

# 7-qadam. test funksiyalari

if __name__ == "main":
    print(hello())
    print(kvadrat(5))
    print(kub(3))
    print(yigindi(5, 7))
    print(ayirma(10, 2))
    print(kopaytma(3, 4))
    print(bolish(20, 5))
    print(max_son(4, 8))
    print(min_son(4, 8))
    print(juftmi(12))
    print(toqmi(7))
    print(katta_harf("python"))
    print(kichik_harf("PYTHON"))
    print(teskari("GitHub"))
    print(uzunligi("Python"))
    print(yigindi_list([1, 2, 3, 4]))
    print(eng_katta([5, 7, 1, 9]))
    print(eng_kichik([5, 7, 1, 9]))
    print(uzunligi_list([1, 2, 3]))
    print(faktorial(5))
    print(daraja(2, 5))
    print(abs_son(-15))