import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return """
    <h1>Hello world</h1>
    <a href="/about">Sobre</a>
    <br>
    <a href="/contact">Contato</a>
  
  """

@app.route('/about')
def about():
  return 'Sobre mim'

@app.route('/contact')
def contact():
  return 'Contato'

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)