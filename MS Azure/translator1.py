# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 14:40:53 2022

@author: yinku
"""
###################################################
import requests, uuid, json
import urllib.request, urllib.parse, urllib.error
import json
import ipywidgets as widgets
import ssl
import requests

#Add your subscription key and endpoint
subscription_key = "292f79c28c9d49bcb5ff08d527a8d6bb"
endpoint = "https://api.cognitive.microsofttranslator.com"
#Azure

#Add your location, also known as region. The default is global.
#This is required if using a Cognitive Services resource.
location = "westeurope"

#If you encounter any issues with the base_url or path, make sure
#that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
path = '/translate?api-version=3.0'

params = {
'api-version': '3.0',
'from': 'en',
'to': 'fr'
}

constructed_url = endpoint + path

headers = {
'Ocp-Apim-Subscription-Key': subscription_key,
'Ocp-Apim-Subscription-Region': location,
'Content-type': 'application/json',
'X-ClientTraceId': str(uuid.uuid4())
}

#You can pass more than one object in body.
body = [{
'text' : 'Hello World!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

infos = json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))


print(response, infos)


'''
info = str(infos)
#i = r"'''" + info + r"'''"
#print(info)
j = info.replace('[', '')
j = j.replace(']', '')
k = r"'''" + j + r"'''"
e = str(k)

#j = str(inf)
#print()
#inf = json.loads(k)
#print('Translation:', k["translation"]["text"])
#print('Language:', info["translation"]["to"])
#print('Translation:', j["translation"])'''


