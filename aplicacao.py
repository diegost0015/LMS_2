from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ListaCursos')
def lista():
    return render_template("LMS_ListaDeCursos.html")


@app.route('/Noticias')
def noticias():
    return render_template("LMS_Noticias.html")


@app.route('/Contato')
def contato():
    return render_template("LMS_Contato.html")


@app.route('/Login')
def login():
    return render_template("LMS_Login.html")


app.run()
