import speech_recognition as sr
import os

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        audio = r.listen(s)

        if r.recognize_google(audio, language='pt') == "educação":

            print("Você disse: ", r.recognize_google(audio, language='pt'))
            os.system('totem ~/Vídeos/educacao.ogv')
        else:
            print("Falhou")
