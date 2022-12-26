# "Banana" Virtual Assistant Copyright (c) 2022-23 Jxcob-Vfx, Jxcob-vfx on Github, Replit, StackOverflow
# TTS Virtual Assistant for quality of life enhancements / experimentation

import os
import time
import playsound
import random
import speech_recognition as sr
from gtts import gTTS

# phrase(s) that alert(s) assistant of a query, akin to "hey google", "alexa", etc.
# it is recommended to use a phrase/phrases with multiple words in this case rather than a single word to prevent accidental activation, as is infamously frequent with alexa
# currently using popular template alert phrases with a NAME constant so that you don't have to change all of the phrases to change the name

NAME = "banana"
ALERT_PHRASES = (f"hey {NAME}", f"okay {NAME}", f"hello {NAME}", f"excuse me {NAME}", f"yo {NAME}")

def speak(args):
	tts = gTTS(text=args, lang="en")
	name = str(hash(args))
	filename = f"{name}.mp3"
	tts.save(filename)
	playsound.playsound(filename)

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		speech = ""
		try:
			speech = r.recognize_google(audio)
			print(speech)
		except Exception as err:
			print(f"Exception: {str(err)}")
	return speech

# tempelate for arguement evaluation

def evaluate(args):
	if foo in args:
		print(bar)
		speak(bar)

def __init__():
	wake = ["Hi, what can I do for you today", "Hi there", "Hello", "Hello there", "Hello. How can I help you today", "Hello. What can I do for you today"]
	while True:
		text = get_audio()

		if ALERT_PHRASE in text:
			speak(wake[random.randint(0,5)])
			args = get_audio()
			evaluate(args)
		else:
			pass

while True:
	__init__()
