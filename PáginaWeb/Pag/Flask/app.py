# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:41:17 2021

@author: SPEs
"""

import io

import ast
#
from flask import Flask, render_template, redirect, request, make_response

import networkx

import matplotlib.pyplot as plt

from base64 import b64encode


#lo que incluye la app y va a servir
app = Flask(__name__, static_url_path="")

#dirige hacia allá
@app.route("/")
def home():
    return redirect("/index.html")

#methods especificar donde se nos pasa la info
@app.route("/module3", methods=("GET", "POST"))
def modulo3transform():
    if request.method == "GET":
        return render_template("/module3.html")
    if request.method == "POST":
        prueba = request.files.get("file")
        if prueba is not None:
            analizar = io.BytesIO()
            prueba.save(analizar)
            analizar.seek(0)
            lectura = analizar.read()
            codigo_ast = ast.parse(lectura)
            variable = graficar(codigo_ast)
            img = b64encode(variable)
            return render_template("render.html", image = img.decode())

    return ""

def graficar(codigo):
    g = networkx.Graph()

    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    networkx.draw(g)
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0) #lee desde el primer byte
    return buffer.read() #retorna array

if __name__ == '__main__':
   		app.run(debug = True)