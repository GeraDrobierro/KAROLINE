graph = {}
graph['интернет'] = ['web', 'map', 'инет', 'паутина']
graph['allMAcBookAppsEng'] = ['открой skype', 'откройка steam', 'open skype', 'open steam']
graph['Karolineworkoff'] = ['закройся', 'stop', 'exit', 'пока', 'bye', 'off', 'стоп']
graph['KarolineMusic'] = ['music', 'музыка', 'melody', 'мелодия']
graph['clock'] = ['clock', 'time', 'alarm', 'покажи время', 'минуты', 'секунды']
graph['программа'] = ['https://www.youtube.com/watch?v=SW_UCzFO7X0', 'часы']
allMAcBookAppsEng = ['skype', 'steam', 'zoom', 'freeform', 'discord', 'google chrome', 'miro', 'tv', 'blender']

import speech_recognition
import os
import sys
import webbrowser
from AppOpener import open


sr = speech_recognition.Recognizer()


def talk(words):
    print(words)
    os.system("say " + words)

def KarolineClosework():
    return talk("Отключаюсь, приятно было поработать"), sys.exit()

def KarolineHello():
    return talk("Здравствуйте")

def KarolineOpenApp():
    return talk("Открываю " + query)



while True:
    with speech_recognition.Microphone() as mic:
        print('Говорите')
        sr.pause_threshold = 1
        sr.adjust_for_ambient_noise(source=mic, duration=1)
        audio = sr.listen(source=mic)
        try:
            query = sr.recognize_google(audio, language='ru').lower()
            print('вы сказали:' + query)
        except speech_recognition.UnknownValueError:
            print('(\(\ ')
            print('(=0:0)')
            print( '(..(")(")')
        if 'try' in query:
            talk('Отлично')
        elif query == 'hello':
            print(KarolineHello())
        elif query in allMAcBookAppsEng or query in graph['allMAcBookAppsEng']:
            print(KarolineOpenApp())
            open(query)
        elif query in graph['интернет']:
            talk('Начинаем серфить интернет')
            url = 'https://www.google.com/?client=safari&channel=iphone_bm'
            webbrowser.open(url)
        elif query in graph['clock']:
            talk('Время не любит, когда его убивают' + query)
            url = 'https://time100.ru/Saint-Petersburg'
            webbrowser.open(url)
        elif query in graph['KarolineMusic']:
            talk('Открываю вашу волну')
            webbrowser.open('https://vk.com/audios371153804')
        elif query in 'сказка':
            talk("Не знаете ли вы, как мне выйти отсюда? – Это зависит от того, куда ты хочешь прийти, – ответил Кот. – Мне все равно, куда бы ни… – начала Алиса. – Значит, тебе все равно, в какую сторону идти, – перебил ее Кот. – Куда бы ни выйти, лишь бы куда-нибудь прийти, – договорила Алиса.")
        elif query in graph['Karolineworkoff']:
            print(KarolineClosework())
        elif query == 'прага':
            webbrowser.open(graph['программа'][0])
        elif query == 'калькулятор':
            a = int(input())
            b = int(input())
            print(talk(str(a+b)))
