from flask import request, Flask
from flask_cors import CORS, cross_origin
import json
import grpc
import os, sys
import re
from io import BytesIO
import base64
from PIL import Image
from tensorflow.keras.preprocessing import image
import tensorflow as tf

from service import Service
from helpers import use_schema

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.append(current_dir)
sys.path.append(parent_dir)
sys.path.append(os.path.dirname(parent_dir))

from grpc_service import service_pb2_grpc as srv_grpc

import validators

app = Flask(__name__)
CORS(app)

BASE_64_HEADER_REGEXP = r'(data:image/.*;base64,)(.*)'


def remove_type_header(image_data):
  """
  Removes the type header added by the browser
  from base64 encoded image data.
  
  Args:
      image_data (str): Encoded image data.
  
  Returns:
      str: the encoded data without the header.
  """
  return re.sub(
    BASE_64_HEADER_REGEXP,
    r'\2',
    image_data
  )

def base64_to_image_array(data):
  """Converts a base4 encoded image
  to an image array.
  
  Args:
      data (string): base64 encoded image.
  
  Returns:
      array: decoded image.
  """
  return Image.open(BytesIO(base64.b64decode(data)))


def load_decoded_img(base_64_img):
  img = base64_to_image_array(remove_type_header(base_64_img))
  img = tf.image.encode_jpeg(image.img_to_array(img))
  return tf.io.encode_base64(img)

@app.route("/predict-salary", methods=['POST'])
@use_schema(validators.PredictSalaryInputSchema())
def predict_salary():
  response = app.config['SERVICE'].predict_salary(int(request.json.get('years')))
  return { 'salary': response.salary, 'success': True }

@app.route("/predict-purchase", methods=['POST'])
@use_schema(validators.PredictPurchaseInputSchema())
def predict_purchase():
  args = request.json
  response = app.config['SERVICE'].predict_purchase(
    int(args.get('age')),
    int(args.get('salary')),
  )
  return { 'purchase': response.purchase, 'success': True }

@app.route("/predict-customer-segment", methods=['POST'])
@use_schema(validators.PredictCustomerSegmentInputSchema())
def predict_customer_segment():
  args = request.json
  response = app.config['SERVICE'].predict_customer_segment(
    int(args.get('anual_income')),
    int(args.get('spending_score')),
  )
  return { 'segment': response.segment, 'success': True }

@app.route("/optimal-campaign-ad", methods=['GET'])
def get_optimal_campaign_ad():
  response = app.config['SERVICE'].get_optimal_campaign_ad()
  return { 'ad': response.ad, 'success': True }

@app.route("/predict-review-outcome", methods=['POST'])
@use_schema(validators.PredictReviewInputSchema())
def predict_review_outcome():
  response = app.config['SERVICE'].predict_review_outcome(
    request.json.get('review'),
  )
  return { 'liked': response.liked, 'success': True }

@app.route("/predict-cat-or-dog", methods=['POST'])
@use_schema(validators.PredictCatOrDogInputSchema())
def predict_cat_or_dog():
  img = load_decoded_img(request.json.get('img'))
  response = app.config['SERVICE'].predict_cat_or_dog(img.numpy())
  return { 'dog': response.dog, 'success': True }

@app.route("/predict-bank-leaving", methods=['POST'])
@use_schema(validators.PredictBankLeavingInputSchema())
def predict_bank_leaving():
  args = request.json
  response = app.config['SERVICE'].predict_bank_leaving(
    credit_score = args.get('credit_score'),
    geography = args.get('geography'),
    gender = args.get('gender'),
    age = args.get('age'),
    tenure = args.get('tenure'),
    balance = args.get('balance'),
    number_of_products = args.get('number_of_products'),
    has_credit_card = args.get('has_credit_card'),
    is_active_member = args.get('is_active_member'),
    estimated_salary = args.get('estimated_salary'),
  )
  return { 'leaving': response.exited, 'success': True }

if __name__ == "__main__":
  print('Server started')

  with grpc.insecure_channel('localhost:50051') as channel:
    client = srv_grpc.MachineLearningStub(channel)
    service = Service(client)
    app.config['SERVICE'] = service
    app.run(
      debug = True,
      port = 3005,
      host = '0.0.0.0',
    )