import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('gveLw5LTT9LcQCu2Lboene_e-lPJXWp9Iw_zEHb-wOh8')

visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com')


with open("C:/Users/harisaik/Desktop/programming/IBM-project/src/test1.jpg", 'rb') as images_file: 
    classes = visual_recognition.classify(images_file=images_file,threshold='0.6',classifier_ids='MaskDetection_736199640').get_result()

print(json.dumps(classes, indent=2))	