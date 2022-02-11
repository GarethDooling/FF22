
from flask import Flask, render_template 

app = Flask(__name__, template_folder='template')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/players')
def players():
    return render_template('players.html')

if __name__ == "__main__":
    app.run(debug=True)
