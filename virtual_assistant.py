''' 
python libraries required:
- pyttsx3 (allow python to 'talk' to us)
- SpeechRecognition (speech to text translation)
- pywhatkit (open and access websites)
- yfinance (Yahoo Finance stock market access)
- pyjokes (library of jokes)
- webbrowser (open webbrowser from code)
- datetime (access date and time)
- wikipedia (access wikipedia)
'''


import pyttsx3
import speech_recognition as sr
import pywhatkit 
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# listen through microphone and return audio as text
def transform_audio_into_text():

    # store recognizer as variable 
    r = sr.Recognizer()

    # set microphone
    with sr.Microphone() as source:

        # waiting time
        r.pause_threshold = 0.8

        # inform that recording as started
        print("Please speak into the microphone.")

        # save audio
        audio = r.listen(source)

        try:
            # search on audio-text on google
            request = r.recognize_google(audio, language="en-US")

            # test in text
            print("You said: " + request)

            # return request
            return request
        
        # audio was not recognized
        except sr.UnknownValueError:

            # inform that audio was not understandable 
            print("I'm sorry. I did not understand what was said.")

            # return error
            return "I am still waiting."

        # audio could not be resolved
        except sr.RequestError:

            # inform that request could not be completed 
            print("I'm sorry. I am unable to complete that request.")

            # return error
            return "I am still waiting."
        
        # Unexpected error
        except:

            # inform that audio was not understandable 
            print("Oops! Something went wrong.")

            # return error
            return "I am still waiting"
        

transform_audio_into_text()