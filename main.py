import random

# Opções do jogador / máquina
opcoes = ['pedra', 'papel', 'tesoura']
# a máquina faz escolhas aleatórias
escolha_computador = random.choice(opcoes)  

# o jogador escolhe 
escolha_jogador = input("Escolha entre pedra, papel ou tesoura: ").lower()

# Verifica se a escolha do jogador é válida
if escolha_jogador not in opcoes:
    print("Escolha inválida. Tente novamente.")
else:
    # As escolhas são comparadas e o vencedor da partida é determinado
    print(f"\nVocê escolheu: {escolha_jogador}")
    print(f"Computador escolheu: {escolha_computador}\n")

  # Caso ambos escolham a mesma opção a partida empata
    if escolha_jogador == escolha_computador:
        print("EMPATE!")
    elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_jogador == 'tesoura' and escolha_computador == 'papel') or \
         (escolha_jogador == 'papel' and escolha_computador == 'pedra'):
        print("VOCÊ VENCEU!")
    else:
        print("O COMPUTADOR VENCEU!")
