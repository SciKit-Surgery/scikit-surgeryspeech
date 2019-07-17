import speech_recognition as sr
import os


class VoiceRecognitionService:

    def __init__(self):
        self.stop_listen = None

        #  this is to add the credentials for the google cloud api
        #  set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path  of your json file with credentials
        key_file_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
        with open(key_file_path, 'r') as file:
            self.credentials = file.read()

    def listen(self):
        # Record Audio
        r = sr.Recognizer()
        m = sr.Microphone()
        #  initialization of the background listening thread
        print("Say something!")
        self.stop_listen = r.listen_in_background(m, self.callback)

    def callback(self, recognizer, audio):
        #  this is called by the background thread, converting speech in a string
        try:
            # google cloud speech to text with credentials (json file)
            words = recognizer.recognize_google_cloud(audio, credentials_json=self.credentials)
            print("You said: " + words)
            #  if the string equals a certain keyword (here "start") the background thread is stopped and the a method
            #  is called to listen to one single command
            if words == "start ":
                self.stop_listen(wait_for_stop=False)
                self.listen_to_command()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def listen_to_command(self):
        r = sr.Recognizer()
        #  listen to a single command
        with sr.Microphone() as source:
            print("Listening for command")
            audio = r.listen(source)
        try:
            #  convert command to string, this string should later be used to fire a certain GUI command
            words = r.recognize_google_cloud(audio, credentials_json=self.credentials)
            print("You said: " + words)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        #  call self.listen() again to get the background thread start listening again
        self.listen()






