# IPDS Ecercise 2
# Functions with parameters

# 16. Conversions

#a)
def hrsToMins (hr):
    m = hr * 60
    return m
def daysToSec (days):
    s = days * 24 * 60 * 60
    return s

#b)
def FtoC (F):
    C = (F-32)*5/9
    return C

#c)
def KmtoM (M):
    Km = M*1.61
    return Km

#d)
def MtoY (M):
    cm = M*100   # 1 inch = 2.54cm
    inch = cm/2.54
    Y = inch / 36   # 1 Yard = 36 inch
    return Y

#e)
def a (n):
    n = int(n)
    return n
