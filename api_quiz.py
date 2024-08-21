from windows_toasts import WindowsToaster, Toast, ToastAudio, AudioSource, ToastDuration, ToastButton
import requests
import json
import sqlite3
import os
from dotenv import load_dotenv


def show_toast(toast, title, msg):
    toast.show_toast(title=title, msg=msg, duration=14)

def joke():
    toaster = WindowsToaster('Python')
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    result = response.json()

    res = json.dumps(result, indent=4)

    with open("chuck_norris.json", "w") as file:
        file.write(res)

    joke_actually = result["value"]
    print(joke_actually)
    newToast = Toast()
    newToast.text_fields = [joke_actually]
    newToast.title = "Chuck Norris Joke"
    newToast.audio = ToastAudio(AudioSource.Reminder, looping=False)
    newToast.duration = ToastDuration(ToastDuration.Short)
    toaster.show_toast(newToast)
    return joke_actually

joke_actually = joke()





# ------------------------------------------
load_dotenv()
api_key = os.getenv("API_KEY")

ex_url = "https://v6.exchangerate-api.com/v6/"

currency_from = input("input 3 main letters of currency you want to exchange: ").upper()

where_to = input("input 3 main letters of currency in which  you want to exchange: ").upper()

amount = float(input("input amount of money you want to exchange: "))

ex_response =  requests.get(ex_url + api_key + "/" + "pair" +"/"+ currency_from + "/" + where_to )

print(ex_response.status_code)

print("*********")

print(ex_response.text)

print("*********")

print(ex_response.content)

print("*********")

print(ex_response.headers)


ex_result  = ex_response.json()
ex_json = json.dumps(ex_result, indent=4)

print(ex_result)
with open ("currency.json" , "w") as ex_file:
    ex_file.write(ex_json)
#  In the documentation, I could not understand how to specify the amount, so I will write a separate code for this:

print("*****************")

print(f"when you exchange {currency_from} to {where_to}\nit's:{amount * ex_result['conversion_rate']}\nrate:{ex_result['conversion_rate']}")



conn = sqlite3.connect("api.sqlite")
curs = conn.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS api_infos
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50),
main VARCHAR(100),
rate FLOAT,
total FLOAT);''')

info_list = [("joke", joke_actually, None,None),
            ("exchange",
             f"{amount} {currency_from} to {where_to}", 
             ex_result['conversion_rate'], 
             amount * ex_result['conversion_rate'])]

curs.executemany("INSERT INTO api_infos (title, main, rate, total) VALUES (?,?,?,?)", info_list)
conn.commit()

conn.close()


