import grpc
import os.path
import tensorflow as tf
from tensorflow.keras.preprocessing import image

from grpc_service import service_pb2 as srv, service_pb2_grpc
from helpers import load_decoded_img

current_dir = os.path.dirname(os.path.realpath(__file__))
images_dir = current_dir + '/models/cat_or_dog_prediction/datasets/'


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = service_pb2_grpc.MachineLearningStub(channel)
        
        salary_response = client.PredictSalary(srv.PredictSalaryRequest(years = 5))
        purchase_response = client.PredictPurchase(srv.PredictPurchaseRequest(age = 47, salary = 30000))
        segment_response = client.PredictSegment(srv.PredictSegmentRequest(annual_income = 20, spending_score = 90))
        ad_response = client.GetOptimalCampaignAdOption(srv.GetOptimalCampaignAdOptionRequest())
        review_response = client.PredictReviewOutcome(srv.PredictReviewOutcomeRequest(review = 'The food was excellent!'))
        bank_leaving_response = client.PredictBankLeaving(srv.PredictBankLeavingRequest(
            credit_score = 502,
            geography = 'France',
            gender = 'Female',
            age = 42,
            tenure = 8,
            balance = 159660.8,
            number_of_products = 3,
            has_credit_card = True,
            is_active_member = False,
            estimated_salary = 113931.57,
        ))

        first_img = load_decoded_img(images_dir, 'cat-rsz.jpg')
        second_img = load_decoded_img(images_dir, 'puppy-rsz.jpg')
        first_cat_or_dog_response = client.PredictCatOrDog(srv.PredictCatOrDogRequest(img = first_img.numpy()))
        second_cat_or_dog_response = client.PredictCatOrDog(srv.PredictCatOrDogRequest(img = second_img.numpy()))

        print('The Salary is = ' + str(salary_response.salary))
        print('Will purchase? = ' + str(purchase_response.purchase))
        print('Segment = ' + str(segment_response.segment))
        print('Ad = ' + str(ad_response.ad))
        print('A like review? = ' + str(review_response.liked))
        print('Bank leaving? = ' + str(bank_leaving_response.exited))
        print('First image is a Dog? = ' + str(first_cat_or_dog_response.dog))
        print('Second image is a Dog? = ' + str(second_cat_or_dog_response.dog))


if __name__ == '__main__':
    run()