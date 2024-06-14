from math import *

# Questão 1:
# Para que dois termos sejam uma PA deve-se verificar se um termo somado a uma razão é igual ao proximo termo.
# Nesse sentido, para saber se dois termos formam uma PG deve-se verificar se um termo multiplicado por uma razão é igual ao proximo termo.
#1º passo: 
# Verificar se os termo da pa ou pg são a e b, e a razão é c;
# Se não, verificar se a e c são termos da pa ou pg, e se c é a razão;


def pag(a,b,c): 
    if (a+c==b) or (a*c==b) : return True
    elif (a+b==c) or (a*b == c) : return True
    elif (b+c==a) or (b*c==a) : return True
    else : return False

#Questão 2:
#Primeiro, verifica-se as codições que alteram o valor do ingresso.
#Supondo um valor vl para o ingresso, temos que:
# Se a idade da pessoa for maior ou igual a 60 anos, pagarão 60% de vl;
# Se a idade da pessoa for até 10 anos o valor do ingresso será 50% de vl;
# Porém, se a idade da pessoa for até 2 anos, paga-se 10% de vl.
#Portanto:

def pgp(vl,i):
    if i>=60 : return 0.6*vl
    elif i>=2 and i<=10 : return 0.5*vl
    elif i<2 : return 0.1*vl
    else: return vl

#Questão 3:
#Para calcular o preço a ser pago pelo aluguel do carro em função da distância e dias de uso,
#deve-se fazer o produto entre o preço por quilometro e distância, e somar com o produto entre o preço por dia e dias rodados.
# Assim:
def rentcar(km,d):
    return km*0.15 + d*60

#Questão 4:
#Para calcular a área sombreada será usada a seguinte ideia: 
# fazer o cáuculo da área do quadrado e subtrair 4 vezez meia pétala de circunferencia, que é a área representada pelas partes em branco da figura.
#Será usado a biblioteca math para usar alguns recursos.
#Ou seja, primeiramente será calculado a área do quadrado com Aquad() e será sbtraido 4 metades de pétala de circunferência que equivale á duas petálas de circunferência que serão calculadas a partir da função ApetCircun().
#Assim:
from math import * 

def area2(l):

    def Aquad(x):
        return x**2
    
    def diagQuad(x):
        return x*sqrt(2)
    
    def ApetCircun(x):
        return (((x/2)**2)*((pi/2)-1))/2
    
    return Aquad(l)-2*ApetCircun(diagQuad(l))
#Questão 5:
#1º passo) Verificar se i e f estão no intervalo de 1 a 366 e se f é maior que i.
#2º passo) Verificar se d está entre i e f;
#           Se for verdadeiro, retornar o valor e;
#           Se for falson retorna o valor 0.

def evento(ag,d):
    (e,i,f) = ag
    if i>=1 and i<=366 and f>i and f<=366:
        if d>=i and d<=f : return e
        else : return 0
    else : return 0


#Questão 6:
#1º passo) Fazer as somas possiveis;
#2º passo) Verificar quais somas deram como resultado um valor multiplo de 5;
#           Se algum valor for multiplo de 5, a função retorna esee valor;
#           Se não, retornar o valor 0.

def pontos(p1,p2):
    (a,b)=p1
    (c,d)=p2
    if (a+c)%5== 0 : return (a+c)
    elif (a+d)%5 == 0 : return (a+d)
    elif (b+c)%5 == 0 : return (b+c)
    elif (b+d)%5 == 0 : return (b+d)
    else : return 0    

