import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import PySimpleGUI as sg

senha = 'cavalo'
saida = 'tchau'
dialogo = 0

layout = [[sg.Text("Vamos conversar")], [sg.Button("OK")]]
window = sg.Window("Conversação", layout)

def cria_audio(audio):
    global dialogo
    tts = gTTS(audio,lang='pt-br')
    path = 'audios/dialogo{}.mp3'.format(dialogo)
    tts.save(path)
    print("Estou aprendendo o que você disse...")
    playsound(path) 
    dialogo = dialogo + 1

def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        if senha in frase:
            tts = gTTS('Porta aberta', lang='pt-br')
            tts.save('audios/segredo.mp3')
            print('você sabe a senha o.o')
            playsound('audios/segredo.mp3')
        print("Você disse: " + frase)
        
    except sr.UnkownValueError:
        print("Não entendi")

    return frase

while True:
    event, values = window.read()
  
    if event == "OK":
        while True:
            frase = ouvir_microfone()
            if saida in frase:
                break
            cria_audio(frase)
        break
    elif event == sg.WIN_CLOSED:
        break
    

window.close()
