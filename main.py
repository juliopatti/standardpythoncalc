# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# [START gae_python38_app]
# [START gae_python3_app]

# A partir do hello word, da documentação em https://cloud.google.com/appengine/docs/standard/python3/runtime
# e do guia para iniciantes em https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-flask-web-calculator.py
# foi montados os primeiros main.py, requirements.txt e app.yaml
# o app.yaml foi adaptado para solicitar um novo serviço e passou a se chamar calculadora.yaml
# versão 2
# um html diretriz foi criado para orientação do usuário
# uma verificação forte de validade da expressão segundo a leitura da função conversora eval() 
# foi realizada para corrigir os erros de conversão da função eval
# tendo o resultado desejado, sem erros de conversão, validação da entrada e da expressão lógica

from flask import Flask, request

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

#@app.route('/')
#def hello():
#    """Return a friendly HTTP greeting."""
 #   return 'Hello World!'
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # show html form
        return '''
            <form method="post">
                <input type="text" name="expression" />
                <input type="submit" value="Calcular" />
                <p>Entre com uma expressão matemática:<p/>
                <html>
                <head>
                <style>
                table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 42%;
                }

                td, th {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
                }

                tr:nth-child(even) {
                background-color: #dddddd;
                }
                </style>
                </head>
                <body>

                <h2>Simbologia de operadores: </h2>

                <table>
                <tr>
                    <th>Símbolo</th>
                    <th>Operação</th>
                </tr>
                <tr>
                    <td>+</td>
                    <td>Adição</td>
                </tr>
                <tr>
                    <td>-</td>
                    <td>Subtração</td>
                </tr>
                <tr>
                    <td>*</td>
                    <td>Multiplicação</td>
                </tr>
                <tr>
                    <td>/</td>
                    <td>Divisão</td>
                </tr>
                <tr>
                    <td>**</td>
                    <td>Exponenciação</td>
                </tr>
                <tr>
                    <td>()</td>
                    <td>Prioridade</td>
                </tr>
                </table>

                </body>
                </html>
            </form>
        '''
    elif request.method == 'POST':
        # calculate result
        expression = request.form.get('expression')
        n=int(len(expression))
        for i in range(0,n):
            if expression[i] in '0123456789+-*/.( )':
                True
            else:
                expression = 'Erro de entrada'
                break
        try:
            result = eval(expression)
            return 'Resultado: %s' % result
        except:
            return 'Expressão Inválida!'

if __name__ == '__main__': 
    app.run(debug=True)

