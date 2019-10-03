# O código original não está errrado, apenas errei quandi passei para o git.
# no indice de nob coloquei number_a ao inves de num_a !





def nob(num_a,num_b):

    dezena_a = num_a // 10
    unidade_a = num_a % 10
    dezena_b = num_b // 10
    unidade_b = num_b % 10

    return unidade_a + dezena_a + unidade_b + dezena_b


def main() :

    print(nob(21,36))

main()
