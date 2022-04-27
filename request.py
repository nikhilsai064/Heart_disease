import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':45, 'sex':1, 'cp':3,'trestbps':192, 'chol':283, 'fbs':0, 'restecg':1,'thalach':195, 'exang':0, 'oldpeak':0.6, 'slope':2, 'ca':0,'thal':3})

print(r.json())