contagem1, contagem2 = 0, 0

def VerificaJogo():
    global tabuleiro2, tabuleiro, jogador1, jogador2, contagem1, contagem2, ganhou1, ganhou2
    #verificação reta = = =
    verifica1, verifica2 = 0, 0
    if verifica1 != 3 and verifica2 != 3:
        for i in range(3):
            verifica1 = 0
            verifica2 = 0
            for j in range(3):
                if tabuleiro2[i][j] == 'X':
                    verifica1 += 1
                elif tabuleiro2[i][j] == 'O':
                    verifica2 += 1
            if verifica1 == 3:
                print('%s ganhou a partida.' %(jogador1))
                contagem1 += 1
                ganhou1 = 1
            elif verifica2 == 3:
                print('%s ganhou a partida.' %(jogador2))
                contagem2 += 1
                ganhou2 = 1
    #verificação transposta
    verifica1, verifica2 = 0, 0
    if verifica1 != 3 and verifica2 != 3:
        for j in range(3):
            verifica1 = 0
            verifica2 = 0
            for i in range(3):
                if tabuleiro2[i][j] == 'X':
                    verifica1 += 1
                elif tabuleiro2[i][j] == 'O':
                    verifica2 += 1
            if verifica1 == 3:
                print('%s ganhou a partida.' % (jogador1))
                contagem1 += 1
                ganhou1 = 1
            elif verifica2 == 3:
                print('%s ganhou a partida.' % (jogador2))
                contagem2 += 1
                ganhou2 = 1
    #verificação diagonal principal
    verifica1, verifica2 = 0, 0
    if verifica1 != 3 and verifica2 != 3:
        for i in range(3):
            if tabuleiro2[i][i] == 'X':
                verifica1 += 1
            elif tabuleiro2[i][i] == 'O':
                verifica2 += 1
        if verifica1 == 3:
            print('%s ganhou a partida.'%(jogador1))
            contagem1 += 1
            ganhou1 = 1
        elif verifica2 == 3:
            print('%s ganhou a partida.'%(jogador2))
            contagem2 += 1
            ganhou2 = 1
    #verificação da diagonal secundária
    verifica1, verifica2 = 0, 0
    if verifica1 != 3 and verifica2 != 3:
        cont1, cont2 = 0, 2
        for i in range(3):
            if tabuleiro2[cont1][cont2] == 'X':
                verifica1 += 1
            elif tabuleiro2[cont1][cont2] == 'O':
                verifica2 += 1
            cont1 += 1
            cont2 -= 1
        if verifica1 == 3:
            print('%s ganhou a partida.'%(jogador1))
            contagem1 += 1
            ganhou1 = 1
        elif verifica2 == 3:
            print('%s ganhou a partida.'%(jogador2))
            contagem2 += 1
            ganhou2 = 1


def fazTabuleiro():
    global tabuleiro2,tabuleiro,jogador1,jogador2
    r = 0
    for i in range(3):
        linha = []
        for j in range(3):
            r += 1
            linha.append(r)
        tabuleiro.append(linha)
    print('Tabuleiro: Posição das peças - de 1 a 9')
    for i in tabuleiro:
        print(i)
    for k in range(3):
        linha1 = []
        for l in range(3):
            o = ''
            linha1.append(o)
        tabuleiro2.append(linha1)
    print("Tabuleiro atual:")
    for m in tabuleiro2:
        print(m)


def imprimeTabuleiro():
    global tabuleiro2,tabuleiro,jogador2,jogador1
    print("Posição das peças:")
    for n in tabuleiro:
        print(n)
    print("Tabuleiro atual:")
    for m in tabuleiro2:
        print(m)


def Jogar():
    global tabuleiro, tabuleiro2, jogador1, jogador2,z, ganhou1, ganhou2, empate
    b = 0 #contador verificador de jogadas
    if ganhou2 != 1 and ganhou1 != 1 and empate != 1:
        if z <= 9:
            while b != 10:
                t = 0
                while t == 0:
                    print(jogador1, "Escolha uma posição no tabuleiro para colocar sua peça: (1 a 9):")
                    try:
                        x = int(input("Digite a posição de sua peça:"))
                    except ValueError:
                        print('Valor inválido')
                    else:
                        t = 1
                for i in range(3):
                    for j in range(3):
                        if tabuleiro[i][j] == x:
                            if tabuleiro2[i][j] != "X" and tabuleiro2[i][j] != "O":
                                tabuleiro2[i][j] = "X"
                                b = 10
                                break
        if z == 9:
            empate = 1
            print('Empatou!')
        z += 1 #contador de jogadas
        imprimeTabuleiro()
        VerificaJogo()
        c = 0 #mesmo contador que o b acima
        if ganhou2 != 1 and ganhou1 != 1 and empate != 1:
            if z <= 9:
                while c != 10:
                    t = 0
                    while t == 0:
                        print(jogador2, "Escolha uma posição no tabuleiro para colocar sua peça: (1 a 9):")
                        try:
                            y = int(input("Digite a posição de sua peça:"))
                        except ValueError:
                            print('Valor inválido')
                        else:
                            t = 1
                    for i in range(3):
                        for j in range(3):
                            if tabuleiro[i][j] == y:
                                if tabuleiro2[i][j] != "X" and tabuleiro2[i][j] != "O":
                                    tabuleiro2[i][j] = "O"
                                    c = 10
                                    break
            z += 1 #contador de jogadas
            imprimeTabuleiro()
            VerificaJogo()

def contador():
    global contagem1,contagem2,partida, jogador1, jogador2
    print('Quantidade de partidas jogadas %i:'%(partida))
    print('Quantidade de partidas que o jogador %s ganhou: %i'%(jogador1, contagem1))
    print('Quantidade de partidas que o jogador %s ganhou: %i '%(jogador2, contagem2))
    if contagem1 > contagem2:
        print('%s é o vencedor geral'%(jogador1))
    elif contagem2 > contagem1:
        print('%s é o vencedor geral'%(jogador2))
    elif contagem1 == contagem2:
        print('Resultado geral deu empate!')

partida = 0 #contador de partidas jogadas
continua = 1 #contador verificador se ganhou partida ou não e também se quer finalizar o jogo
jogador1 = str(input("Nome do jogador 1:"))
jogador2 = str(input("Nome do jogador 2:"))
while continua != 0:
    empate = 0
    tabuleiro = []  # matriz para mostrar a posição das peças
    tabuleiro2 = []  # matriz para as peças dos jogadores
    fazTabuleiro()
    z = 1 #contador de jogadas (9 jogadas total max)
    ganhou1, ganhou2 = 0, 0
    while z < 10 and ganhou1 != 1 and ganhou2 != 1 and empate != 1:
        Jogar()
        if empate == 1:
            continua = 0
            while continua != 1:
                try:
                    continua = int(input("%s, deseja uma nova partida? (Sim - 1 Não - 0)"%(jogador1)))
                except ValueError:
                    print('Valor inválido')
                else:
                    if continua == 1:
                        partida += 1
                    elif continua == 0:
                        print('Obrigado, jogador %s.'%jogador1)
                        contador()
                    break
        if ganhou1 == 1:
            continua = 0
            while continua != 1:
                try:
                    continua = int(input("%s, deseja uma nova partida? (Sim - 1 Não - 0)"%(jogador1)))
                except ValueError:
                    print('Valor inválido')
                else:
                    if continua == 1:
                        partida += 1
                    elif continua == 0:
                        print('Obrigado, jogador %s.'%jogador1)
                        contador()
                    break
        elif ganhou2 == 1:
            continua = 0
            while continua != 1:
                try:
                    continua = int(input("%s, deseja uma nova partida? (Sim - 1 Não - 0)"%(jogador2)))
                except ValueError:
                    print('Valor inválido')
                else:
                    if continua == 1:
                        partida += 1
                    elif continua == 0:
                        print('Obrigado, jogador %s.'%(jogador2))
                        contador()
                        break




