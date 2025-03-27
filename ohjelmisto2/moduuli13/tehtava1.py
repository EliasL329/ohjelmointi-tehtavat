from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    alkuluku = True

    for i in range(2, luku):
        if luku // i == luku / i:
            alkuluku = False
    
    vastaus ={
        "Number":luku, "isPrime":alkuluku
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)