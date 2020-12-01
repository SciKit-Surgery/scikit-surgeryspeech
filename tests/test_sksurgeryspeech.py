# coding=utf-8

"""scikit-surgeryspeech tests"""

import mock
import pytest

from sksurgeryspeech.algorithms.voice_recognition_service import VoiceRecognitionService

# Can't test properly without a microphone (or a Google Cloud API Key), so
# just do some simple checks to catch any silly errors.
@mock.patch('pvporcupine.create')
@mock.patch('pyaudio.PyAudio.open')
def test_setup_voice_recognition(mocked_create, mocked_open):

    config = {"porcupine dynamic library path": ".",
              "porcupine model file path": ".",
              "porcupine keyword file": "."}

    service = VoiceRecognitionService(config)

    service.run()

    service.request_stop()

def test_missing_config_keys_raise_errors():

    config = {}

    with pytest.raises(KeyError):
        service = VoiceRecognitionService(config)

    config = {"porcupine dynamic library path": "."}

    with pytest.raises(KeyError):
        service = VoiceRecognitionService(config)

    config = {"porcupine dynamic library path": ".",
              "porcupine model file path": "."}

    with pytest.raises(KeyError):
        service = VoiceRecognitionService(config)