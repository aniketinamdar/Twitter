from flask import Flask, jsonify, request
from flask_cors import CORS
from model import *

app = Flask(__name__)

CORS(app)

default_values = {
    "tweet":None,
    "prompt":None
}

@app.route('/')
def home():
  return 'Backend server running'

@app.route('/analysis', methods=['GET'])
def get_fundamental():
    print(request.args)
    tweet = request.args.get('twt')
    prompt = get_analaysis_prompt(tweet)
    resp = get_analysis(prompt)
    return resp

if __name__ == "__main__":
   from waitress import serve
   serve(app, host="0.0.0.0", port=8080)