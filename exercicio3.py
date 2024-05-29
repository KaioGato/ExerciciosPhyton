
def conta(c):
    if c<=5 : return 50
    elif c>5 and c<10 : return 50+10*(c%5)
    elif c==10 : return 100
    elif c>10 : return 5*c

#Tabela de testes
#Parametro c || resposta da funcao
#   2        ||         50
#   5        ||         50 
#   6        ||         60
#   7        ||         70
#   8        ||         80
#   9        ||         90
#   10       ||        100
#   11       ||         55
#   25       ||        125
