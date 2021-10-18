import pandas as pd
import json
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection('drugs').stream()

for doc in docs:
    print(doc)

# datas = json.load(open("./drug1.json"))['results']

# for data in datas:
#     try:
#         print(data['openfda']['brand_name'][0])
#         print(data['openfda']['generic_name'][0])
#         print(data['openfda']['manufacture_name'][0])
#         print(data['purpose'][0])
#         print(data['warnings'][0])
#         print(data['openfda']['route'][0])
#         print(data['dosage_and_administration'][0])
#         print(data['adverse_reactions'][0])
#     except Exception as e:
#         pass