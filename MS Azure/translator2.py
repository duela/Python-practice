# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 15:10:07 2022

@author: yinku
"""

import requests, uuid, json

# Add your key and endpoint
key = "292f79c28c9d49bcb5ff08d527a8d6bb"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "westeurope"

path = '/translate?api-version=3.0'


params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['fr', 'zu', 'de']
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': key,'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'I would really like to drive your car around the block a few times!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
