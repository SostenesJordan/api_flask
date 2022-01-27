from flask import Flask, jsonify
from models.ngo import NGO, NGOEncoder
from db import db

app = Flask(__name__)

app.config['DEBUG'] = True

app.json_encoder = NGOEncoder

@app.route('/')
def index():
    return '<h1>Rotas:</h1><br> <p>Dados:</p><strong><a href="/api/v1/resources/ngos"><code>/api/v1/resources/ngos</code></strong></a>'

@app.route('/api/v1/resources/ngos', methods=['GET'])
def list_all():
    return jsonify({'ngos': db})

app.run()