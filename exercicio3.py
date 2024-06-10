
def conta(c):
    if c<=5 : return 50
    elif c>5 and c<10 : return 50+10*(c%5)
    elif c==10 : return 100
    elif c>10 : return 5*c

#Tabela de testes
#Parametro c || resposta esperada || resposta da funcao 
#   2        ||         50        ||        50
#   5        ||         50        ||        50
#   5.5      ||         55        ||        55
#   6        ||         60        ||        60
#   7        ||         70        ||        70
#   8        ||         80        ||        80
#   9        ||         90        ||        90
#   10       ||        100        ||       100
#   10.3     ||         51.5      ||        51.5
#   11       ||         55        ||        55  
#   25       ||        125        ||       125
