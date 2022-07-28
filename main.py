from flask import Flask, render_template, request
from modules import des

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jeux', methods=['GET', 'POST'])
def jeux():
  mon_tirage = des.tirage_des().tirage()
  choix_joueur = request.form.get('le_pari')
  print (choix_joueur)
  resultat = des.tirage_des().verification(choix_joueur,mon_tirage)
  return render_template('page_jeux.html', resu=resultat, tira=mon_tirage)


#app.run(host='0.0.0.0', port=81)