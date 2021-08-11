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
                <input type="submit" value="Calculate" />
            </form>
        '''
    elif request.method == 'POST':
        # calculate result
        expression = request.form.get('expression')
        result = eval(expression)
        return 'result: %s' % result

if __name__ == '__main__': 
    app.run(debug=True)

