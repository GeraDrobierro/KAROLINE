### KAROLINE

# ВСТУПЛЕНИЕ
Вся моя работа над вопросно-ответной системой 'KAROLINE' началась с комадны `say`, введеной в терминал, которая заставила мой компьютер возпроизвести последующую за ней строку `Hello my friend`

Далее в python, я написал простенький код, чтобы проверить одну теорию:

```
import os
a = str(input())
If a == “привет”
print(os.system(‘say ‘ + ‘привет, меня зовут Каролина’))
```

И вот оно. В первый раз заговорили с женским полом, шучу. Этот код позволил убедиться в следующей теории. Я ввёл некую ключевую команду строчного типа, а потом сделал так, чтобы на этот ключ реагировала наша программа, и это сработало. Из всего этого следует, что я могу задать n-количество ключевых команд, и Каролина будет на них реагировать.

Но мы хотим, чтобы она сумела не только говорить с нами, мы хотим, чтобы она нас слушала, выполняла различные команды. И таким образом, я плавно перехожу к следующему пункту, а именно оставлению блок-схемы или roadmap Каролины.



## библиотеки
Из поставленных в roadmap задач для того, чтобы создать мою Каролину мне нужно было что-то, что могло бы слышать мою речь и переводить ее в строку. Для этого, благо, на Python существует библиотека Speech_Recognition. Обо всем ее функционале в полном объёме объясняют [здесь](https://vc.ru/dev/286441-raspoznavanie-i-analiz-rechi-s-pomoshchyu-biblioteki-speech-recognition-pyaudio-i-librosa). Мне же нужно было только то, что с помощью этой библиотеки можно записывать речь с микрофона и преобразовать ее в  строчный формат. Далее, модуль [webbrowser](https://docs.python.org/3/library/webbrowser.html), он позволит работать с url ссылками и открывать их. 
Библиотека [AppOpener](https://pypi.org/project/appopener/), данная библиотека позволит работать с приложениями, установленными на моем компьютере. Модуль [sys](https://pythonim.ru/moduli/sys-python) нужен будет в будущем для того, чтобы остановить работу Каролины по ключевому слову. Сейчас самый важный модуль - os. Проследите за логической цепочкой: say является одной из команд операционной системы, python просто так с ним работать не будет, он попросту не понимает что такое say, поэтому нам нужно что-то, что позволяло бы работать с этой командой, и решением этого вопроса станет библиотека [os](https://all-python.ru/osnovy/os.html#chto-takoe-modul-os).

## установка необходимых библиотек


## код

Сначала импортируем необходимый нам библиотеки, чтобы мы могли с ними работать
```
import speech_recognition
import os
import sys
import webbrowser
import pyaudio
from AppOpener import open
```
Так, теперь, постоянно прописывать `os.system(‘say ‘ + ‘текст’)` неудобно, долго, муторно и друг к негативные прилагательные. Cоздадим функцию, с помощью которой будет говорить Каролина 
