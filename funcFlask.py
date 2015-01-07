# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template

import sqlite3

app = Flask(__name__)

@app.route("/")
def renderform():
	return render_template('index.html')

@app.route("/agregar/", methods=['POST'])
def renderBusqueda():
	busqueda = request.form['busqueda']
	conn = sqlite3.connect('baseDatos')
	c=conn.cursor()
	query=c.execute("SELECT marca, modelo, precio, tipo, valoracion, tienda, imagen, fecha, caracteristicas FROM dispositivo where modelo=(?) ORDER BY precio",(busqueda,))
	conn.commit()
	#conn.close()
	return render_template('listaProductos.html', productos=query)

@app.route("/agregar/", methods=['POST'])
def 

if __name__ == "__main__":
      app.run(debug=True)