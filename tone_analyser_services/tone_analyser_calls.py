import json
import requests
from urllib.parse import quote
from config.config_reader import config_data
from requests.auth import HTTPBasicAuth

tone_analyser_version = '/v3/tone?version=2017-09-21'


def get_tone_from_text(text):
    return json.dumps(requests.get(config_data()['tone_analyser_url'] + tone_analyser_version + '&text=' + quote(text), auth=HTTPBasicAuth('apikey', config_data()['api_key'])).json(), indent=2)


def get_text_tone_from_json_file(file_location):
    headers = {'content-type': 'application/json'}
    with open(file_location) as json_file:
        json_text = json.load(json_file)
        return json.dumps(requests.post(config_data()['tone_analyser_url'] + tone_analyser_version, auth=HTTPBasicAuth('apikey', config_data()['api_key']),
                             headers=headers, json=json_text).json(), indent=2)


