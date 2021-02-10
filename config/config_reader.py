import json
from definitions import ROOT_DIR


def config_data():
    with open(ROOT_DIR + '/config/config.json') as config:
        return json.load(config)

