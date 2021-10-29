from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/mostraEstoque', methods=['post', 'get'])
def mostraEstoque():
    with open('estoque.json', 'r') as arq:
        valorEstoque = json.loads(arq.readline())
    print(valorEstoque)
    return render_template('mostraEstoque.html', dados=valorEstoque)


if __name__ == '__main__':
    app.run()
