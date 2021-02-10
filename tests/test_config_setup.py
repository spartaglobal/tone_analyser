import os
from definitions import ROOT_DIR
from config.config_reader import config_data

base_tone_analyser_url = "https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/"

def test_config_file_is_created():
    assert os.path.isfile(ROOT_DIR + '/config/config.json')


def test_config_file_contains_api_key():
    assert len(config_data()['api_key']) > 0


def test_config_file_contains_correct_end_point():
    assert base_tone_analyser_url in config_data()['tone_analyser_url']