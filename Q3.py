def pi(n):

    resultado=0
    valor=0
    contador=0

    for contador in range (0,n):

        valor = 4 * (((-1)**(contador))/((2*contador)+1))

        resultado += valor
    
    return resultado


def main() :

    n = 1

    while (módulo(pi(n)-pi(n-1)) > 5*10**(-8)) :

        print(pi(n))

        n+=1

main()