from flask import Flask
import mysql.connector

app = Flask(__name__)
@app.route('/hae_lentokentta/<ICAO>')

def hae_lentokentta(ICAO):

    yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port= 3306,
            database='flight_game',
            user='root',
            password='root',
            autocommit=True,
            collation='utf8mb3_unicode_ci'
            )

    sql = f"SELECT ident, name, municipality from airport where ident ='{ICAO}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    return  {"ICAO":tulos[0][0], "Name":tulos[0][1], "Municipality":tulos[0][2]}




if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)