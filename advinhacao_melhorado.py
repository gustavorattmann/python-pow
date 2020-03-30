import random # Importa o módulo random

print("*******************************")
print("Seja bem-vindo ao jogo da advinhação!!!!")
print("*******************************")

num_secret = int(random.random() * 100) # Cria um número aleatório até 100, para ser advinhado
total_de_tentativas = 3 # Quantas tentativas a pessoa terá

'''
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = int(input("Digite um número: "))

    acertou = chute == num_secret
    maior = chute > num_secret

    if (acertou):
        print("Você acertou!!!!")
        break
    else:
        if (maior):
            print("Você errou! Número digitado maior que o número secreto!")
        else:
            print("Você errou! Número digitado menor que o número secreto!")

    rodada = rodada + 1
'''

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = int(input("Digite um número entre 1 e 100: "))

    if(chute < 1 or chute > 100):
        print("Digite apenas números entre 1 e 100!")
        continue
    else:
        acertou = chute == num_secret
        maior = chute > num_secret

        if(acertou):
            print("Você acertou!!!!")
            break
        else:
            if(maior):
                print("Você errou! Número digitado maior que o número secreto!")
            else:
                print("Você errou! Número digitado menor que o número secreto!")

        if(rodada >= total_de_tentativas):
            print("Número correto era", num_secret)

print("Fim de jogo")