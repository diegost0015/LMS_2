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


@app.route('/Curso1')
def curso1():
    return render_template("LMS_DetalheCurso1.html")


@app.route('/Curso2')
def curso2():
    return render_template("LMS_DetalheCurso2.html")


@app.route('/Curso3')
def curso3():
    return render_template("LMS_DetalheCurso3.html")


@app.route('/Curso4')
def curso4():
    return render_template("LMS_DetalheCurso4.html")


@app.route('/Curso5')
def curso5():
    return render_template("LMS_DetalheCurso5.html")


@app.route('/Curso6')
def curso6():
    return render_template("LMS_DetalheCurso6.html")


@app.route('/Disciplina1')
def Disciplina1():
    return render_template("Disciplina1.html")


@app.route('/Disciplina2')
def Disciplina2():
    return render_template("Disciplina2.html")


@app.route('/Disciplina3')
def Disciplina3():
    return render_template("Disciplina3.html")


@app.route('/Disciplina4')
def Disciplina4():
    return render_template("Disciplina4.html")


@app.route('/Disciplina5')
def Disciplina5():
    return render_template("Disciplina5.html")


@app.route('/Disciplina6')
def Disciplina6():
    return render_template("Disciplina6.html")


app.run()
