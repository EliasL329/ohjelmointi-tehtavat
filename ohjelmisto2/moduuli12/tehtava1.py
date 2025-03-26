import requests

def main():
    vitsi = requests.get("https://api.chucknorris.io/jokes/random").json()

    print(vitsi["value"])

main()