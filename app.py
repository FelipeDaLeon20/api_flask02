from flask import Flask, render_template as render, request
import math
app = Flask(__name__)

@app.route('/index')
def home():
    titulo = "pagina de inicio"
    listado = ['Python','Flask,','Jinja2','HTML','CSS']
    return render('index.html',titulo=titulo,listado=listado)

@app.route('/calculos',methods=('GET','POST'))
def about():
    if request.method == 'POST':
        numero1 = request.form['numero1']
        numero2 = request.form['numero2']
        operacion = request.form['operacion']
        if operacion == 'suma':
            res = int(numero1) + int(numero2)
            nOp='suma'
        if operacion == 'resta':
            res = int(numero1) - int(numero2)
            nOp='resta'
        if operacion == 'multiplicacion':
            res = int(numero1) * int(numero2)
            nOp='multiplicacion'
        if operacion == 'division':
            res = int(numero1) / int(numero2)
            nOp='division'
        return render('calculos.html', res=res,numero1=numero1,numero2=numero2,nOp=nOp)
    return render('calculos.html')

    return render('calculos.html')

@app.route('/distancia',methods=('GET','POST'))
def distancia():
    if request.method == 'POST':
        x1 = request.form['x1']
        x2 = request.form['x2']
        y1 = request.form['y1']
        y2 = request.form['y2']
        difx = int(x2)-int(x1)
        dify = int(y2)-int(y1)
        res = math.sqrt((difx*difx) + (dify*dify))
        return render('distancia.html', x1=x1,x2=x2,y1=y1,y2=y2,difx=difx,dify=dify,res=res)
    return render('distancia.html')

@app.route('/user/<string:user>')
def user(user):
    return f"Hola ,{user}"

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1,num2):
    return f"La suma es: {num1+num2}"

@app.route('/numero/<int:num>')
def func(num):
    return f"El numero es {num}"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {} nombre: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def func1(n1,n2):
    return "la suma es :{}".format(n1+n2)

@app.route("/default")
@app.route("/default/<string:dft>")
def func2(dft="sss"):
    return "el valor de dft es "+dft

@app.route("/prueba")
def func3():
    return ''' 
    <html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hola amigos de youtube</h1>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    -->
  </body>
</html>
    
    '''





if __name__ == '__main__':
    app.run(debug=True)