import PySimpleGUI as sg

sg.theme('GreenMono') 

layout = [[sg.Text('Enter Text:'), sg.InputText(key='input')],
          [sg.Text('Select Voice:'), sg.Radio('Male', "RADIO1", default=True, key='male'), sg.Radio('Female', "RADIO1", key='female')],
          [sg.Button('Speak'), sg.Button('Exit')]]

window = sg.Window('Text to Speech', layout)

import pyttsx3

def speak(text, voice_type='male', volume=2.5, speed=1.5):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voice_type == 'male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume', volume)
    engine.setProperty('rate', speed*200)
    engine.say(text)
    engine.runAndWait()

while True:
      event, values = window.read() 

      if event == sg.WIN_CLOSED or event == 'Exit': 
        break

      if event == 'Speak': 
        text = values['input']
        voice_type = 'male' if values['male'] else 'female'
        speak(text, voice_type=voice_type)

window.close() 



print('hello world')



      




 
