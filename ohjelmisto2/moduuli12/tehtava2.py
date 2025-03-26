import requests

appid = ""

def main():
    kunta = input("Syötä kunta: ")
    geoHaku = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={kunta}&appid={appid}").json()

    saaHaku = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={geoHaku[0]['lat']}&lon={geoHaku[0]['lon']}&appid={appid}&lang=fi").json()

    lampotila = saaHaku['main']
    saa = saaHaku['weather'][0]

    print(f"Lämpötila: {round(lampotila['temp'] - 273.15, )} °C\nSää: {saa['description']}")

main()
