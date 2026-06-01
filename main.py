import random

forca = [
r"""
  +---+
  |   |
      |
      |
      |
      |
""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
"""
]

animais = ['macaco', 'tigre', 'avestruz', 'mamute', 'rinoceironte', 'cobra']
países = ['china', 'austrália', 'turquia', 'venezuela','brasil', 'mexico', 'argentina' ]
cores = ['amarelo', 'vermelho', 'verde','azul']

print('============Jogo da forca============')
while True:
    tema = int(input('Escolha um dos temas:\n[1]-ANIMAIS\n[2]-PAÍSES\n[3]-CORES\n[4]-SAIR DO JOGO'))

    if tema == 4:
        print('Jogo finalizado')
        break

    elif tema == 1 or tema == 2 or tema == 3:
        erro=0
        if tema == 1:
            escolhido = random.choice(animais)
            tracos = ["—"] * len(escolhido)
        elif tema == 2:
            escolhido = random.choice(países)
            tracos = ["—"] * len(escolhido)
        elif tema == 3:
            escolhido = random.choice(cores)
            tracos = ["—"] * len(escolhido)

        while tracos.count('—') > 0 and erro<6:
            print( forca[erro])
            print(" ".join(tracos))
            # join é um metodo que junta elementos de uma lista em uma string
            letra = str(input('Escolha uma letra:'))
            if letra in escolhido:
                for i in range(0,len(escolhido)):
                    if escolhido[i]== letra:
                            tracos[i] = letra
            else:
                    erro+=1
        if tracos.count('—') == 0:
                print('VOCÊ GANHOU!!!')
                print(forca[erro])
                print(" ".join(tracos))
        if erro==6:
                print("\nPERDEU 💀")
                print(forca[erro])
                print(" ".join(tracos))
    else:
        print('Opção inválida, digite novamente: ')



