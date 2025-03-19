import mysql.connector, geopy.distance

def hae_lentokentta(ICAO):

    sql = f"SELECT latitude_deg, longitude_deg from airport where ident ='{ICAO}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    return tulos

def main():
    ICAO1 = input("Syötä 1. lentokentän ICAO koodi: ")
    a = hae_lentokentta(ICAO1)
    ICAO2 = input("Syötä 2. lentokentän ICAO koodi: ")
    b = hae_lentokentta(ICAO2)

    print(geopy.distance.distance(a, b).kilometers)

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True,
         collation='utf8mb3_unicode_ci'
         )

main()