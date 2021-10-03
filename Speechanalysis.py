##  The code is used for the analysis aspect of the project. 
##  This code takes the waveform as input and does two things: 
##  1) passes the waveform for analysis. 
##  2) Converts audio to text for detecting keywords like ‘happy’, ‘sad’, etc. 
##  It returns the keyword and mood as a result."""


import json
import Record
import os
from ibm_watson import ToneAnalyzerV3
from os.path import join, dirname 
from ibm_watson import SpeechToTextV1 
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 


def speechtext():
    print('Recording Started')
    Record.record()
    if(os.path.exists('myfile.wav')==True):
        print('recording complete')
    authenticator = IAMAuthenticator('PDkEi3h3AkbNqldQGxu8qJVm7JojaJ2X--xdX1k8b9aj')# Paste the Authorisation token
    service = SpeechToTextV1(authenticator = authenticator)

    #Paste the authorisation url
    service.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/dfef8b97-384a-48ed-a446-969a821a2372') 

    with open(join(dirname('__file__'), r'myfile.wav'), 'rb') as audio_file:
        dic = json.loads(
            json.dumps( 
                    service.recognize( 
                        audio=audio_file, 
                        content_type='audio/wav', 
                        model='en-US_NarrowbandModel', 
                    continuous=True).get_result(), indent=2))

    str = "" 

    while bool(dic.get('results')): 
        str = dic.get('results').pop().get('alternatives').pop().get('transcript')+str[:]

    
    return str



def analysis():
    authenticator = IAMAuthenticator('Bp6npJ89891S23rprtJHyg_Pg_3MMWYzayU1fLM0SS_j') # Paste the authorisation token
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )

    # Paste the authorisation url
    tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/1077e8e7-9ad4-4449-858d-b34f77fb1c40')

    text=speechtext()

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()

    os.remove('myfile.wav')

    try:
        tone=tone_analysis["document_tone"]["tones"][0]["tone_id"]
        #print(tone)
        return tone+' '+text
    except:
        pass
    return text
