import os

class Config(object):
    API_KEY = os.environ.get('OWM_KEY') or '31d0868c88f01425a8ae7b049433dca4'