import letters
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        letraEscolhida = request.form['choice']
        letra = request.form['letra']
        resultado = letters.aferir(letra, letraEscolhida)
        letters.say(resultado)
        return render_template('index.html', resultado=resultado)
    letra = letters.letra()
    letters.say("Olá Laurinha! vamos brincar com as letras?")
    letters.say(f'Onde esta a letra {letra}?')
    return render_template('index.html', letra=letra)


if __name__ == '__main__':
    app.run(debug=True)



