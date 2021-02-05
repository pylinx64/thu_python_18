import pyttsx3
import webbrowser

tts = pyttsx3.init()            # Инициализировать голосовой движок

tts.setProperty('voice', 'en')  # Наш голос по умолчанию
tts.setProperty('rate', 150)    # Скорость в % (может быть > 100)
tts.setProperty('volume', 0.8)  # Громкость (значение от 0 до 1)


def say_assistant(msg): 
    '''Бот говорит фразу'''
    tts.say(msg)     
    tts.runAndWait() # Воспроизвести очередь реплик

def open_web(msg):
    '''Открываем браузер'''
    if 'открой' in msg.lower():
        reg_ex = re.search('открой (.+)', msg)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain + '.com'
            webbrowser.open(url)
            say_assistant('Sait otkrit, ')
        else:
            pass

NAME = 'moye imya Dori bot'
say_assistant(NAME)
while True:
	COMMAND_MSG = 'Enter the command: '
	say_assistant(COMMAND_MSG)
	command = input(COMMAND_MSG)
	if 'привет' in command:
		say_assistant('nu privet')
	elif 'пушкин' in command:
		say_assistant('''
		drfsgfdgfdgfdgfg
		''')
	elif 'как дела' in command:
		say_assistant('norm')
	elif 'погода' in command:
		say_assistant('norm +5')
	elif 'браузер' in command:
		webbrowser.open('https://www.youtube.com/')
		say_assistant('browser open')
	else:
		say_assistant('ya tebya ne ponimayu pshchpfshchshch')
