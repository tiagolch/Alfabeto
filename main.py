import letters
from flask import Flask, render_template, request 


app = Flask(__name__)


@app.route('/<string:name>', methods=['GET', 'POST'])
def index(name):
    if request.method == 'POST':
        choice = request.form['choice']
        letter = request.form['letter']
        result = letters.gauge(letter, choice, name)
        letters.say(result)
        return render_template('index.html', result=result, name=name)
    letter = letters.letter()
    letters.say(letters.salutation(name))
    letters.say(f'Onde esta a letra {letter}?')
    return render_template('index.html', letter=letter, name=name)


if __name__ == '__main__':
    app.run(debug=True)



