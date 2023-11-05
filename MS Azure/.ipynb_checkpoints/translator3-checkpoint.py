# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 22:30:42 2022

@author: yinku
"""

import urllib.request, urllib.parse, urllib.error
import json
import ipywidgets as widgets
import ssl
import requests

def azure_translate(text):
    API_KEY = "292f79c28c9d49bcb5ff08d527a8d6bb"
    API_REGION = "westeurope"
    
    endpoint = 'https://api.cognitive.microsofttranslator.com/'
    headers = {'Ocp-Apim-Subscription-Key': API_KEY,
               'Content-type': 'application/json', 
               'Ocp-Apim-Subscription-Region': API_REGION}
    params = {'api-version': '3.0', 'from': 'es', 'to': 'fr'}
    api_url = endpoint + 'translate'
    body = [{'text': text}]
    response = requests.post(api_url, params=params, headers=headers, json=body)
    return response.json()

if __name__ == '__main__':
    print(azure_translate('Hola.'))
    
info = str(azure_translate('Hola.'))


def on_button_clicked(b):
    response = azure_translate(w_text.value)
    w_output.clear_output()
    with w_output:
        print(response[0]['translations'][0]['text'])

w_header = widgets.HTML('<h2><i>SIMPLE</i> <b>Translator</b></h2>')
w_text = widgets.Textarea(placeholder='Write something!', layout=widgets.Layout(width = '80%'))
w_button = widgets.Button(description='Translate To Spanish')
w_button.on_click(on_button_clicked)
w_output = widgets.Output()
w_ui = widgets.VBox([w_header, w_text, w_button, w_output], layout=widgets.Layout(align_items='center'))
display(w_ui)