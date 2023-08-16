#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python Program that helps translate Speech to Text and vice-versa


# In[2]:


import speech_recognition
import pyttsx3
import voices
from googletrans import Translator


# In[3]:


engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name}")
    print(f"Voice: {voice.id}")


# In[4]:


# The Recognizer is initialized.
engine = pyttsx3.init()
UserVoiceRecognizer = speech_recognition.Recognizer()


# In[5]:


def getLanguage(argument):
    switcher = {
        0: "en-IN",
        6: "hi-IN",
        5: "zh-CN",
        4: "ko-KR",
        3: "ja-JP",
        1: "de-de"
    }
    return switcher.get(argument, 0)


# In[6]:


def get_Language(argument):
    switcher = {
        0: "en",
        6: "hi",
        5: "zh-CN",
        4: "ko",
        3: "ja",
        1: "de"
    }
    return switcher.get(argument, "en")


# In[7]:


def getSelection():
    while True:
        try:
            userInput = int(input())
            if userInput < 0 or userInput > 6:
                print("Not an integer! Try again.")
                continue
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break


# In[8]:


translator = Translator()


# In[ ]:


while 1:
    try:
        print("Select your language:")
        print("0. ENGLISH")
        print("6. HINDI")
        print("5. Chinese")
        print("4. KOREAN")
        print("3. JAPANESE")
        print("1. GERMAN")
        lang = getLanguage(getSelection())

        with speech_recognition.Microphone() as UserVoiceInputSource:
            UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)

            # The Program listens to the user voice input.
            UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
            UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput, language=lang)
            UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.lower()
            print("Detected Text:", UserVoiceInput_converted_to_Text)

            print("0. ENGLISH")
            print("6. HINDI")
            print("5. Chinese")
            print("4. KOREAN")
            print("3. JAPANESE")
            print("1. GERMAN")
            tran = getSelection()
            lang = get_Language(tran)
            print("Selected Language:", lang)
            translated_text = translator.translate(UserVoiceInput_converted_to_Text, dest=lang)
            translation_result = translated_text.text
            print("Translated Text:", translation_result)
            voices = engine.getProperty('voices')
            if len(voices) > 0:
                desired_voice = voices[tran].id  # Use the first voice in the list
                engine.setProperty('voice', desired_voice)
            else:
                print("No voices available.")
            #engine.setProperty('rate', 145)
            engine.setProperty('voice', lang)
            engine.say(translation_result)
            # play the speech
            engine.runAndWait()

            #engine.setProperty('voice', lang)  # Set the desired language voice
            #engine.say(translation_result)
            #engine.runAndWait()

    except KeyboardInterrupt:
        print('A KeyboardInterrupt encountered; Terminating the Program !!!')
        exit(0)

    except speech_recognition.UnknownValueError:
        print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!! \n CAN YOU PLEASE DO IT AGAIN")


# In[ ]:




