# coding=utf-8
from sksurgeryspeech.algorithms import first_test_speech_api as speech_api
import time
"""Speech api demo module"""


def run_demo():
    voice_recog = speech_api.first_test_speech_api()
    voice_recog.listen()
    for _ in range(200):
        time.sleep(0.1)


