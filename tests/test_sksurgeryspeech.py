# coding=utf-8

"""scikit-surgeryspeech tests"""

# Pytest style
from platform import platform 
from sksurgeryspeech.algorithms import voice_recognition_service as speech_api

def test_voice_recognition_service():
    if platform == "Linux":
        config = {
            "porcupine dynamic library path" : ".tox/py36/lib/python3.6/site-packages/pvporcupine/lib/linux/x86_64/libpv_porcupine.so",
            "porcupine model file path" : ".tox/py36/lib/python3.6/site-packages/pvporcupine/lib/common/porcupine_params.pv",
            "porcupine keyword file" : [".tox/py36/lib/python3.6/site-packages/pvporcupine/resources/keyword_files/linux/jarvis_linux.ppn"],
            "timeout for command" : 1,
            "sensitivities" : [1.0],
            "interval": 10,
            "recogniser" : "testing",
            "test signals" : [
                ["start_listen", False],
                ["google_api_not_understand", False],
                ["google_api_request_failure", "the internet is broken"],
                ["voice_command", "next"],
                ["voice_command", "previous"],
                ["voice_command", "next"],
                ["start_processing_request", False],
                ["unknown_command", "what's this"],
                ["voice_command", "quit"]],
        }
    elif platform == "Windows":
        config = {
            "porcupine dynamic library path" : ".tox/py36/lib/python3.6/site-packages/pvporcupine/windows/x86_64/libpv_porcupine.dll",
            "porcupine model file path" : ".tox/py36/lib/python3.6/site-packages/pvporcupine/lib/common/porcupine_params.pv",
            "porcupine keyword file" : [".tox/py36/lib/python3.6/site-packages/pvporcupine/resources/keyword_files/windows/porcupine_windows.ppn"],
            "timeout for command" : 1,
            "sensitivities" : [1.0],
            "interval": 10,
            "recogniser" : "testing",
            "test signals" : [
                ["start_listen", False],
                ["google_api_not_understand", False],
                ["google_api_request_failure", "the internet is broken"],
                ["voice_command", "next"],
                ["voice_command", "previous"],
                ["voice_command", "next"],
                ["start_processing_request", False],
                ["unknown_command", "what's this"],
                ["voice_command", "quit"]],
        }
    else:
    config = {
            "porcupine dynamic library path" : ".tox/py36/lib/python3.6/site-packages/pvporcupine/mac/x86_64/libpv_porcupine.dylib",
            "porcupine model file path" : ".tox/py36/lib/python3.6/site-packages/pvporcupine/lib/common/porcupine_params.pv",
            "porcupine keyword file" : [".tox/py36/lib/python3.6/site-packages/pvporcupine/resources/keyword_files/mac/porcupine_mac.ppn"],
            "timeout for command" : 1,
            "sensitivities" : [1.0],
            "interval": 10,
            "recogniser" : "testing",
            "test signals" : [
                ["start_listen", False],
                ["google_api_not_understand", False],
                ["google_api_request_failure", "the internet is broken"],
                ["voice_command", "next"],
                ["voice_command", "previous"],
                ["voice_command", "next"],
                ["start_processing_request", False],
                ["unknown_command", "what's this"],
                ["voice_command", "quit"]],
        }


    voice_recognition = speech_api.VoiceRecognitionService(config)
    voice_recognition.run() 
