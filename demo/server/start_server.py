from flask import request, Flask
from flask_cors import CORS, cross_origin
import json
import sys

app = Flask(__name__)

CORS(app)

@app.route("/", methods=['POST'])
def test():
  return "Worked"

@app.route("/up", methods=['GET'])
def up():
    return "I am up"

if __name__ == "__main__":
  print('Start server')
  app.run(
    debug = True,
    port = 3005,
    host = '0.0.0.0',
  )