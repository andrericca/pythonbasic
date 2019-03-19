from random import randint
print ('Bem vindo ao jogo de adivinhação!')
sorteado = randint (1,100)
# print (sorteado)
chute = 0
while chute !=sorteado:
    limite_sorteado = 100*0.05
    x = sorteado-limite_sorteado
    y = sorteado+limite_sorteado
    g=input ('Chute um número: ')
    chute = int(g)
    if chute == sorteado:
        print ('Você venceu, parabéns!')
    if x<chute<y:
        print ('Você passou perto!')
    elif chute > sorteado:
        print('Chutou alto demais')
    else: 
        print ('Chutou baixo demais')
print ('Fim de jogo!')