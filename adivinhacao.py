import random

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0

print('qual o nivel de dificuldade?')
print('1 - fácil, 2- médio, 3- difícil')
nivel = int(input('Digite o nivel: '))

if  nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print(f'tentativas {rodada} de {total_de_tentativas}')
    valor_escolhido_str = input('Digite um número entre 1 a 100: ')
    print('você digitou', valor_escolhido_str)
    valor_escolhido = int(valor_escolhido_str)
    
    if valor_escolhido < 1 or valor_escolhido > 100:
        print('Número Inválido, o número deve ser entr 1 e 100')
        continue
    
    acertou = valor_escolhido == numero_secreto
    maior = valor_escolhido > numero_secreto
    menor = valor_escolhido < numero_secreto
    
    if acertou:
        print('Parabéns você acertou o número secreto')
        break
    else: 
        if maior:
            print('Você errou, o número escolhido foi maior que o número secreto')
        elif menor:
            print('Você errou, o número escolhido foi menor que o número secreto')
print('Fim de Jogo')
    
