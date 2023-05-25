from win10toast import ToastNotifier
import requests
import json
import sqlite3


def joke():
    global joke_actually
    toast = ToastNotifier()
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    result = response.json()

    res = json.dumps(result, indent=4)

    with open("chuck_norris.json", "w") as file:
        file.write(res)

    joke_actually = result["value"]
    print(joke_actually)
    toast.show_toast(title='New joke', msg=joke_actually, duration=14)


joke()





# ------------------------------------------

api_key = "564f99316c38fb22304897a2"
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
# დოკუმენტაციაში ვერ გავიგე როგორ მივუთითო რაოდენობა და გადაიყვანოს ამიტომაც ამისათვის ცალკე დავწერ კოდს:
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
             ("exchange", f"{amount} {currency_from} to {where_to}", ex_result['conversion_rate'], amount * ex_result['conversion_rate'])]
curs.executemany("INSERT INTO api_infos (title, main, rate, total) VALUES (?,?,?,?)", info_list)
conn.commit()

conn.close()


