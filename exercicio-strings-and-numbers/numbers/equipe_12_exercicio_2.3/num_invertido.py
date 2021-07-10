#equipe 12 - 2. Grupo: Questões com Números
#Desenvolver um programa, usando a Linguagem de Programação Phyton, para ler um
#número inteiro positivo. Em seguida, desenvolver funções para:

#2.3 Imprimir o número invertido; Exemplo: Entrada: 864 Saída: 468


#Scrum master: Lucas
#Devs:
#Lucas Miranda
#Victor  Levy
#Maikon Anderson
#Lucas Miranda


def entradaInt(msg):
    ok = False
    while True:
        n = input(msg)
        if n.isnumeric():
            n = int(n)
            ok = True
        else:
            print('CARACTER INCORRETO, FAVOR DIGITE UM NUMERO INTEIRO')
        if ok:
            break
    return n

def retorna_numeroInvertido (num):
  numInvertido = str(num)[::-1]
  return numInvertido

# Função sem parâmetro, que retorna uma mensagem com a saída do dado
def print_mensagem ():
    print("O número invertido é:",retorna_numeroInvertido(n))

n = int(entradaInt('Digite um numero inteiro: '))
print_mensagem() #Chama função mensagem
input("Pressione alguma tecla para finalizar") # Finaliza o programa