from flask import Flask, render_template
import pickle

app = Flask(__name__)
modelo = pickle.load(open('../../models/modelo.pkl', 'rb'))


@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)