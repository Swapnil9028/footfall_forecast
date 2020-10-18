import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Imp Festivals':1, 'Less Imp Festivals':0, 'No Holiday':29, 'weekend':13,'noofEvents':1, 'campaignPriority':1, 'marketingSpend':20000})

print(r.json())