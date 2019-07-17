# coding=utf-8
from sksurgeryspeech.algorithms import first_test_speech_api as speech_api
import time
"""Speech api demo module"""


def run_demo():
    #  this is the main call to start the background thread listening,
    #  which also later has to be called within the SmartLiver code

    voice_recognition = speech_api.VoiceRecognitionService()
    voice_recognition.listen()
    for _ in range(500):
        time.sleep(0.1)


