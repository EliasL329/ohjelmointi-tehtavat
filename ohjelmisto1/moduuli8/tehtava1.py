import mysql.connector

def hae_lentokentta(ICAO):

    sql = f"SELECT name from airport where ident ='{ICAO}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    print(tulos)

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True,
         collation='utf8mb3_unicode_ci'
         )
 
ICAO = input("Syötä lentokentän ICAO koodi: ")
hae_lentokentta(ICAO)