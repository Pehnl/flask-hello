import os
import json
import pickle
import sklearn
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
  try:
    # Receber o arquivo do formulario
    file = request.files['file']

    # Enviar o arquivo para a API
    response = requests.post(
      'https://face.ifelseonline.com.br/encoding',
      files={'file': (
        file.filename,
        file.stream,
        file.content_type,
        file.headers
      )}
    )

    # Decodificar resposta
    data = json.loads(response.text)

    # Verificar se a resposta teve sucesso
    if not data['success']:
      return render_template(
        'predict.html',
        predict='Sem faces'
      )

    # Enviar as caracteristicas para o modelo
    face_enconding = data['encodings']
    clf = pickle.load(open('clf.picle', 'rb'))
    predict = clf.predict([face_enconding])[0]

    print(data)
  except Exception:
    return render_template(
      'predict.html',
      predict="erro ao reconhecer face"
    )

  return render_template(
    'predict.html',
    predict=predict
  )

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)