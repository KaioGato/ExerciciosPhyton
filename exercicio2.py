from math import *

def intervalo(x):
    return (x>=0) and (x<=100)

def divisivel(x): 
    return x%15==0

def xp(n): return intervalo(n) and divisivel(n)

def raio_circulo(d): 
    return d/2

def area_circulo(r): 
    return pi*r*r

def area_quadrado(l):
    return l*l

def lado_quadrado(d):
    return  d/sqrt(2)

def amarelo(x1,y1,x2,y2):
    d = (y1-y2)
    return area_quadrado(lado_quadrado(d))-area_circulo(raio_circulo(lado_quadrado(d))) 