import random
import pyttsx3

alphabet = 'abcdefghijklmnoprstuvwxyz'

def say(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', "brazil")
    engine.setProperty('rate', 190)
    engine.say(text)
    engine.runAndWait()

def salutation(name):
    return f'Olá {name}! vamos brincar com as letras?'

def letter():
    letter = random.choice(alphabet)  
    return letter

def gauge(letter, choice, name='Fulano'):
    if letter == str(choice):
        return f'Parabens {name}, Acertou Miseravi!'
    return 'Infelizmente você não acertou.'
