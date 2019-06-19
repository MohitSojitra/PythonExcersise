import requests






def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")

data = requests.get('https://newsapi.org/v2/everything?q=bitcoin&from=2019-05-06&sortBy=publishedAt&apiKey=c995496803fb498eb6d30f38c8e3bcd1')



data = data.json
speak("hello mohit")
