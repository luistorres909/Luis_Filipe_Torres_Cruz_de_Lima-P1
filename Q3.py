Durante a prova me esqueci se existia algum operador para módulo, e pensei em
fazer esta função, porém fiquei receoso de colocar mais uma função no programa.
Segue a função que retira o valor absoluto de um número. Além disso, ao realizar
a questão considerei que deveria exibir todos os valor de pi(n) conforme n aumenta
e caminha para o caso em que sua diferença seja a requisitada na questão, assim
podemos ver que pi(n) se aproxima de pi conforme n cresce !



def mod(n):
    if (n >= 0):

        return n
    
    if (n < 0) :

        return -n    



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

    while (mod(pi(n)-pi(n-1)) > 5*10**(-8)) :

        print(pi(n))

        n+=1

main()