# coding=utf-8
"""
Demo for the Speech API module
"""
import time
import logging
from sksurgeryspeech.algorithms import first_test_speech_api as speech_api


def run_demo():
    """
    Entry point to run the demo
    :return:
    """
    #  this is the main call to start the background thread listening,
    #  which also later has to be called within the SmartLiver code
    root_logger = logging.getLogger("voice_recognition_logger")
    root_logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    root_logger.addHandler(handler)

    voice_recognition = speech_api.VoiceRecognitionService()
    voice_recognition.listen()
    for _ in range(500):
        time.sleep(0.1)
