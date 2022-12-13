"""

Jogo para o usuário adivinhar qual
a palavra secreta

"""




palavra_secreta = 'paisagem'
letras_acertadas =''
tentativas = 0
tentativas_erradas = 0
maximo_tentativas = 3
while True:
    letra_digitada = input('Digite apenas uma letra')
    
    tentativas += 1

    if len(letra_digitada)> 1: 
        print('Digite apenas uma letra')
        continue
        
    if letra_digitada in palavra_secreta:

        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else: 
            palavra_formada += '*'
            tentativas_erradas +=1
          

    print('Palavra formada', palavra_formada)
    print('Tentativas', tentativas)

  