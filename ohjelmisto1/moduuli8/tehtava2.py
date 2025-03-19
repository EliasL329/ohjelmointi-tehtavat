import mysql.connector

def hae_lentokentat(maakoodi):

    lentokentat = {}

    sql = f"select type from airport where iso_country = '{maakoodi}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    for i in tulos:
        if i not in lentokentat:
            lentokentat[i] = 1
        else:
            lentokentat[i] += 1

    return lentokentat

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True,
         collation='utf8mb3_unicode_ci'
         )

maakoodi = input("Syötä maakoodi: ")
sanakirja = hae_lentokentat(maakoodi)

for i in sanakirja:
    print(i, sanakirja[i])