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


# Voice options
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

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


# give voice to assistant
def speak(message):

    # start pyttsx3
    engine = pyttsx3.init()

    # set voice option
    engine.setProperty('voice', id2)

    # deliver message
    engine.say(message)
    engine.runAndWait()


# inform day of the week
def ask_day():

    # variable with today's information
    day = datetime.date.today()

    # variable for day of the week
    week_day = day.weekday()

    # name of day corresponding to each number
    calendar = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}

    # say day of the week
    speak(f'Today is {calendar[week_day]}')


# inform of current time
def ask_time():

    # variable with current time information
    time = datetime.datetime.now()
    time = f'At this moment, it is {time.hour} hours and {time.minute} minutes.'

    # say time
    speak(time)


# initial greeting
def initial_greeting():

    # say greeting
    speak("Hello Kevin. I am your personal assistant. How can I help you?")


# main function of assistant
def my_assistant():

    # start with initial greeting
    initial_greeting()

    # cut-off variable
    go_on = True

    while go_on:

        # activate the microphone and save request
        my_request = transform_audio_into_text().lower()

        if 'open youtube' in my_request:
            speak('Sure, I am opening youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open browser' in my_request:
            speak('Of course, I am on it')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is it' in my_request:
            ask_day()
            continue
        elif 'what time is it' in my_request:
            ask_time()
            continue
        elif 'do a wikipedia search for' in my_request:
            speak("I am searching Wikipedia")
            # strip voice command, leaving only subject to be searched
            my_request = my_request.replace('do a wikipedia search for', '')
            answer = wikipedia.summary(my_request, sentences=1)
            speak("According to Wikipedia: ")
            speak(answer)
            continue
        elif 'search the internet for' in my_request:
            speak("Will do, right away")
            my_request = my_request.replace('search the internet for', '')
            pywhatkit.search(my_request)
            speak("This is what I found")
            continue
        elif 'play' in my_request:
            speak("Oh, what a great idea. I'll play it right now")
            my_request = my_request.replace('play', '')
            pywhatkit.playonyt(my_request)
            continue
        elif 'joke' in my_request:
            speak((pyjokes.get_joke()))
            continue
        elif 'stock price' in my_request:
            share = my_request.split()[-1].strip()
            portfolio = {
                'apple': 'APPL',
                'amazon': 'AMXN',
                'google': 'GOOGL',
            }

            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info['regularMarketPrice']
                speak(f"I found it! The price of {share} is {price}")
                continue
            except:
                speak("I am sorry but I wasn't able to find it")
                continue
        elif 'goodbye' in my_request:
            speak("I am going to rest. Let me know if you need anything. Byebye! ")
            break


my_assistant()