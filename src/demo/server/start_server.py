from flask import request, Flask
from flask_cors import CORS, cross_origin
import json
import grpc
import os, sys
from service import Service

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.append(current_dir)
sys.path.append(parent_dir)
sys.path.append(os.path.dirname(parent_dir))

from grpc_service import service_pb2_grpc as srv_grpc

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def test():
  return "Worked"

@app.route("/up", methods=['GET'])
def up():
  return "I am up"

@app.route("/predict-salary", methods=['GET'])
def predict_salary():
  response = app.config['SERVICE'].predict_salary(int(request.args.get('years')))
  return { 'salary': response.salary }

@app.route("/predict-purchase", methods=['GET'])
def predict_purchase():
  response = app.config['SERVICE'].predict_purchase(
    int(request.args.get('age')),
    int(request.args.get('salary')),
  )
  return { 'purchase': response.purchase }

def create_app(service):
  app.config['SERVICE'] = service
  return app

if __name__ == "__main__":
  print('Start server')

  with grpc.insecure_channel('localhost:50051') as channel:
    client = srv_grpc.MachineLearningStub(channel)
    service = Service(client)
    created_app = create_app(service)
    created_app.run(
      debug = True,
      port = 3005,
      host = '0.0.0.0',
    )