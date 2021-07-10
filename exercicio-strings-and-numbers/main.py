from functions import fn_DivSub
from functions import fn_Palindrome
from functions import fn_Hiperfatorial

x = fn_DivSub.fn_Divisao(10, 10)
y = fn_DivSub.fn_Subtracao (10, 10)

hiperfatorial = fn_Hiperfatorial.fn_Hiperfatorial(3)

print(hiperfatorial)
print(x)
print(y)

#Chamada da Função de Palindromo
frase = str(input('Digite uma frase: ')).strip().upper()
verificaTamanhoDaString(frase)

