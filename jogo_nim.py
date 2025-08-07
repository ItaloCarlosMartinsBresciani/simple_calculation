def escolher():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    escolha = int(input())
    partida(escolha)

def partida(escolhe):  
    
    if escolhe == 1:
        print("Voce escolheu uma partida isolada!")
        e_campeonato = 0
        pontuacao_pc = 0
        pontuacao_usuario = 0
        partida_isolada(e_campeonato, pontuacao_pc, pontuacao_usuario)
    elif escolhe == 2:
        print("Voce escolheu um campeonato!")
        e_campeonato = 1
        pontuacao_pc = 0
        pontuacao_usuario = 0
        campeonato(e_campeonato, pontuacao_pc, pontuacao_usuario)
    else:
        print("Valor inválido")
        escolher()


def partida_isolada(e_campeonato, pontuacao_pc, pontuacao_usuario):
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    if n % (m+1) == 0:
        print("Você começa!")
        usuario_escolhe_jogada(n, m, e_campeonato, pontuacao_pc, pontuacao_usuario)
    else:

        print("Computador começa!")
        computador_escolhe_jogada(n, m, e_campeonato, pontuacao_pc, pontuacao_usuario)
       

def computador_escolhe_jogada(total, retirada, e_campeonato, pontuacao_pc, pontuacao_usuario):
    retirar = retirada 
    while (total - retirar) % retirada != 0:
        retirar -= 1
    
    total = total - retirar
    print("O computador tirou", retirar, "\n")
    print("Agora restam", total, "peças no tabuleiro.\n")     
    
    if total == 0:
        print("Fim do jogo! O computador ganhou!") 
        if e_campeonato >= 1:
            pontuacao_pc += 1
            
            if pontuacao_pc == 3 or pontuacao_usuario + pontuacao_pc == 3:
                print ("**** Final do campeonato! ****")
                print("Placar: Você ",pontuacao_usuario," X ", pontuacao_pc, " Computador")
            else:
                campeonato (e_campeonato, pontuacao_pc, pontuacao_usuario)
        return   
    else:
        usuario_escolhe_jogada(total, retirada, e_campeonato, pontuacao_pc, pontuacao_usuario)



def usuario_escolhe_jogada(max, retirada, e_campeonato, pontuacao_pc, pontuacao_usuario):
    
    tirar = int(input("Quantas peças você vai tirar?\n"))
    while tirar > retirada:
        print("Oops! Jogada inválida! Tente de novo.")
        tirar = int(input("Quantas peças você vai tirar?\n"))
        
    resto = max - tirar
    print("Você tirou", tirar, "peças.")
    print("Agora resta", resto, "peças no tabuleiro\n")
    if (resto == 0):
        print("Fim do jogo! O você ganhou!")
        if e_campeonato >= 1:
            pontuacao_usuario += 1
            if pontuacao_usuario == 3 or pontuacao_usuario + pontuacao_pc == 3:
                print ("**** Final do campeonato! ****\n\n")
                print("Placar: Você ",pontuacao_usuario," X ", pontuacao_pc, " Computador")
            else:
                campeonato (e_campeonato, pontuacao_pc, pontuacao_usuario)
        return
    else:
        computador_escolhe_jogada(resto, retirada, e_campeonato, pontuacao_pc, pontuacao_usuario)


def campeonato(e_campeonato, pontuacao_pc, pontuacao_usuario):
    
    print("\n**** Rodada ",e_campeonato,"****\n")
    e_campeonato += 1
    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? \n"))
    
    while m >=  n:
        print("Numeros inválidos\n")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? \n"))
      
    if n % (m+1) == 0:
        print("Você começa!\n")
        usuario_escolhe_jogada(n, m, e_campeonato, pontuacao_pc, pontuacao_usuario)
    else:

        print("Computador começa!\n")
        computador_escolhe_jogada(n, m, e_campeonato, pontuacao_pc, pontuacao_usuario)

escolher()