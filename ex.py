# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:47:42 2023
@author: WRF
"""
#1=======================================

def get_valeur (p,x):
    valeur = 0
    for i in range (len(p)):
        valeur += p[i]*(pow(x,i))
    return valeur

def get_derivee (p,x):
    derivee = 0
    for i in range (len(p)):
        derivee += p[i]*i*(pow(x,i-1))
    return derivee
"""
l = int(input("Taille du tableau du coefficients a :"))
p = [0]*l
for i in range (0,l):
    p[i] = float(input())
x = float(input("Veuillez entrer le point à calculer : "))
print("La valeur polynôme du point x : ",get_valeur(p, x))
print("La valeur dérivée du point x : ",get_derivee(p, x))
"""
#2=======================================
def dichotomie0(p, x_min, x_max, eps):
    c = 0.0
    pA = 0.0
    pB = 0.0
    pC = 0.0
    a = x_min
    b = x_max
    pA = get_valeur(p, a)
    pB = get_valeur(p, b)
    if pA == 0:
        return a
    elif pB == 0:
        return b
    else:
        while pC!=0 and b-a>eps:
            c = (a+b)/2
            pC = get_valeur(p, c)
            if pA*pC<0:
                b = c
                pB = pC
            else:
                a = c
                pA = pC
        return c

def dichotomie(p,a,b,eps):
    c=(a+b)/2
    result1=get_valeur(p,a)
    result2=get_valeur(p,b)result3=get_valeur(p,c)
    if result1==0:
        print(f"{a}est la resolution")
        return a
    elif result2==0:
        print(f"{b}est la resolution")
        return b
    while result3!=0 and b-a>eps:
        c=(a+b)/2result3 = get_valeur(p, c)
        if result1 * result3<0:
            b=c
            result2=result3
        else:
            a=c
            result1=result3
        print(c)

def newton(p,x0,eps):
    uN = 0.0
    uN = eps + 1
    while get_valeur(p, x0) != 0 and abs(uN)>eps:
        uN = get_valeur(p,x0)/get_derivee(p, x0)
        x0 = x0 - uN
    return x0

def binary_search_root(f, a, b, tolerance):
    if f(a) * f(b) >= 0:
        raise ValueError("函数f(a)和f(b)必须具有不同的符号")

    while (b - a) / 2.0 > tolerance:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c  # 找到精确根
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0  # 返回近似根

def polynome(p,x):
    for i in range(1,len(p)):
        print(f"{p[i]}*x^{i}+",end='')
    print(f"{p[-1]}",end='')


l = int(input("Ordre du polynôme : "))
p = [0]*(l+1)
for i in range (l+1):
    print("p[",i,"] = ",end='')
    p[i] = float(input())
print("Pour méthode dichotomique :")
a = float(input("coefficient d'invervalle a = "))
b = float(input("coefficient d'invervalle b = "))
print("Pour méthode Newton : ")
x0 = float(input("valeur initaile x0 = "))
eps = float(input("Précision eps = "))
print("Racine par dichotomique : ",dichotomie(p, a, b, eps))
print("Racine par Newton : ",newton(p, x0, eps))


