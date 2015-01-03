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
	query=c.execute("SELECT marca,modelo,valor,valoracion,tienda,pantalla, camara FROM smarthphone where marca=(?) ORDER BY valor",(busqueda,))
	conn.commit()
	#conn.close()
	return render_template('listaProductos.html', productos=query)


if __name__ == "__main__":
      app.run(debug=True)