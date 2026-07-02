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