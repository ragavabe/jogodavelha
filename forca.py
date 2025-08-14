def mostrar(tabuleiro, altura, largura):
    for i in range(altura):
        print(" | ".join(tabuleiro[i]))
        if i < altura - 1:
            print("-" * (largura * 4 - 1))

tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
altura = largura = 3
ch = "O"
n_jogadas = 0

while True:
    mostrar(tabuleiro, altura, largura)

    entrada = input('\nIntroduza a posição linha/coluna (separado por espaço): ')
    partes = entrada.split()

    if len(partes) != 2 or not all(p.isdigit() for p in partes):
        print("*** Entrada inválida! Use: número espaço número ***")
        continue

    lin, col = map(int, partes)
    if not (1 <= lin <= altura and 1 <= col <= largura):
        print("*** Valores fora do tabuleiro ***")
        continue

    lin -= 1
    col -= 1

    if tabuleiro[lin][col] != " ":
        print('Posição ocupada\nJogue Novamente!!!')
        continue

    ch = 'X' if ch == 'O' else 'O'
    tabuleiro[lin][col] = ch
    n_jogadas += 1

    for i in range(altura):
        if tabuleiro[i].count(ch) == largura:  
            mostrar(tabuleiro, altura, largura)
            print(f"Jogador {ch} venceu!")
            exit()

    for j in range(largura):
        if all(tabuleiro[i][j] == ch for i in range(altura)):  
            mostrar(tabuleiro, altura, largura)
            print(f"Jogador {ch} venceu!")
            exit()

    if all(tabuleiro[i][i] == ch for i in range(altura)): 
        mostrar(tabuleiro, altura, largura)
        print(f"Jogador {ch} venceu!")
        exit()

    if all(tabuleiro[i][largura - 1 - i] == ch for i in range(altura)):
        mostrar(tabuleiro, altura, largura)
        print(f"Jogador {ch} venceu!")
        exit()

    if n_jogadas == altura * largura:
        mostrar(tabuleiro, altura, largura)
        print('*** Empate técnico ***')
        break