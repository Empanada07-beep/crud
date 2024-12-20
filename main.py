from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL



app = Flask(__name__)


mysql=MySQL()

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_PORT"]=3306
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="dbcrud"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/clientes")

def index_clientes():
    
    sql="SELECT * FROM clientes"

    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql)
    clientes=cursor.fetchall()
    conexion.commit()
    return render_template("/modulos/clientes/index.html", clientes=clientes)




@app.route("/clientes/create")
def create():
    return render_template("/modulos/clientes/create.html")


@app.route("/clientes/create/guardar", methods=["POST"])
def clientes_guardar():
    cedula=request.form["cedula"]
    nombre=request.form["nombre"]
    apellido=request.form["apellido"]
    telefono=request.form["telefono"]
    fecha=request.form["fecha"]
    
    sql="INSERT INTO clientes(cedula, nombre, apellido, telefono, fecha) VALUES(%s, %s, %s, %s, %s)"
    datos=(cedula, nombre, apellido, telefono, fecha)
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect("/clientes")

@app.route("/clientes/edit/<cedula>")
def clientes_editar(cedula):
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM clientes WHERE cedula=%s",(cedula,))
    clientes=cursor.fetchone()
    conexion.commit()
    return render_template("/modulos/clientes/edit.html", clientes=clientes)
    

@app.route("/clientes/edit/actualizar", methods=["POST"])
def clientes_actualizar():
    cedula=request.form["txtcedula"]
    cedula=request.form["cedula"]
    nombre=request.form["nombre"]
    apellido=request.form["apellido"]
    telefono=request.form["telefono"]
    fecha=request.form["fecha"]
    
    sql="UPDATE clientes set nombre=%s, apellido=%s telefono=%s, fecha=%s WHERE cedula=%s"
    datos=(nombre, apellido, telefono, fecha, cedula)
    
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect("/clientes")
    
@app.route("/clientes/borrar/<cedula>")
def clientes_borrar(cedula):
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE cedula=%s",(cedula,))
    conexion.commit()
    return redirect("/clientes")
   


if __name__ == '__main__':
    app.run(debug=True)
    
    