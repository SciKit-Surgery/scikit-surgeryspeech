import speech_recognition as sr

class first_test_speech_api:

    def __init__(self):
        self.stop_listen = None

    def listen(self):
        # Record Audio
        r = sr.Recognizer()
        m = sr.Microphone()
        #  with sr.Microphone() as source:
        print("Say something!")
        #  audio = r.listen(source)
        self.stop_listen = r.listen_in_background(m, self.callback)
        # Speech recognition using Google Speech Recognition

    def callback(self, recognizer, audio):
        try:
            # default google api key
            words = recognizer.recognize_google(audio)
            print("You said: " + words)
            if words == "start":
                self.stop_listen(wait_for_stop=False)
                self.listen_to_command()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def listen_to_command(self):
        r = sr.Recognizer()
        m = sr.Microphone()

        with sr.Microphone() as source:
            print("Listening for commands")
            audio = r.listen(source)
        try:
            words = r.recognize_google(audio)
            print("You said: " + words)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        self.listen()






