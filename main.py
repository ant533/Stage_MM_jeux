from flask import Flask, render_template
from modules import des

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jeux', methods=['GET', 'POST'])
def jeux():
  mon_tirage = des.tirage_des().tirage()
  return render_template('page_jeux.html', resultat="gagné", tira=mon_tirage)


app.run(host='0.0.0.0', port=81)