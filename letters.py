import random
import pyttsx3

alfabeto = 'abcdefghijklmnoprstuvwxyz'

def say(texto):
    engine = pyttsx3.init()
    engine.setProperty('voice', "brazil")
    engine.setProperty('rate', 190)
    engine.say(texto)
    engine.runAndWait()

def letra():
    letra = random.choice(alfabeto)  
    return letra

def aferir(letra, letraEscolhida):
    if letra == str(letraEscolhida):
        return 'Parabens Laurinha, Voce acertou!'
    return 'Infelizmente você não acertou.'
