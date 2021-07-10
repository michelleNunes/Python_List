# Definição da função do cálculo do superfatorial
# Entrada: um número inteiro
def fn_superFatorial(n):
    auxN = 1
    aux = []
    # Calcula o fatorial do número
    for i in range(1, n + 1):
        auxN = auxN * i
        aux.append(auxN)

    res = [1]
    # Calcula o superfatorial do número
    for i in range(1, len(aux)):
        res.append((res[-1] * aux[i]))
    return res[-1]


# Recebendo o input do usuário para o cálculo do superfatorial
int_n = int(input("Digite um número para o qual deseja o fatorial: "))
# Usando o input do usuário como entrada para a função do superfatorial
sf = fn_superFatorial(int_n)
# Imprime o valor do superfatorial
if (int_n>=0):
    print("O superfatorial de {} é {}.".format(int_n,sf))
else:
    print("numero invalido, insira um número inteiro positivo")