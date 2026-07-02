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