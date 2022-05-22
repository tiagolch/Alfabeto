'''
Algoritmo alfabeto:
Ao selecionar a opção alfabeto o programa deve informar que ira solicitar algumas 
letras afim testar o conhecimento do usuario.

1 - O sistema informa uma letra por audio aleatoriamente.
2 - Espera-se que o usuario digite um caracter seguido de enter para imputar automaticamente.
3 - O sistema compara o caracter imputado com a letra informada.
4 - Caso verdadeiro é dado parabens, caso contrário é informado sobre o erro e pede para imputar o
caracter novamente.
'''

import random
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 120)
alfabeto = 'abcdefghijklmnoprstuvwxyz'

def letra():
    letra = random.choice(alfabeto)
    engine.say(f'Digite a letra {letra}')
    print(letra)
    engine.runAndWait()
    return letra

def aferir(letra, letraEscolhida):
    if letra == letraEscolhida:
        return 'Parabens, Voce acertou!!'
    return 'Hummm, Infelizmente esta incorreto.'


engine.say("Olá, vamos ver se voce acerta algumas letras?")
engine.say("Lets go")

letra = letra()

letraEscolhida = input('---> ' )


resultado = aferir(letra, letraEscolhida)
engine.say(resultado)
engine.runAndWait()
    
print(resultado)
