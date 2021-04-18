# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:41:17 2021

@author: SPEs
"""

import io

import ast
#
from flask import Flask, render_template, redirect, request

import networkx as nx

import matplotlib.pyplot as plt

from base64 import b64encode

#lo que incluye la app y va a servir
app = Flask(__name__, static_url_path="")

#dirige hacia allá
@app.route("/")
def home():
    return redirect("/index.html")

#methods especificar donde se nos pasa la info, donde va templates también
@app.route("/module3", methods=("GET", "POST"))
def modulo3transform():
    if request.method == "GET":
        return render_template("/module3.html")
    if request.method == "POST":
        archivo = request.files.get("file")
        archivo2 = request.files.get("file2")
        if archivo is not None:
            #archivo virtual
            analizar = io.BytesIO()
            archivo.save(analizar)
            #desde índice 1
            analizar.seek(0)
            lectura = analizar.read()
            codfor_ast = ast.parse(lectura)
            almacen = imgrafos(codfor_ast)

            #hace el encode para ver imagen
            img = b64encode(almacen)
            return render_template("render.html", image = img.decode())

        elif archivo2 is not None:
            #archivo virtual
            analizar = io.BytesIO()
            archivo2.save(analizar)
            #desde índice 1
            analizar.seek(0)
            lectura = analizar.read()
            codfor_ast = ast.parse(lectura)
            almacen = imgrafos(codfor_ast)

            #hace el encode para ver imagen
            img = b64encode(almacen)
            return render_template("render.html", image = img.decode())

    return ""

def imgrafos(codigo):
    g = nx.DiGraph()

    # almacenamiento apoyo
    clase = []
    metodos = []
    listaargumentos = []
    listaatributos = []
    dicc_argum = {}

    # hallar clases y métodos y agregarlos a listas
    # por cada nodo en to_do el cuerpo de lo leído, si es una clase, agregue a clase
    for nodo in codigo.body:
        if isinstance(nodo, ast.ClassDef):
            clase.append(nodo)
        # por cada clase en clase, por cada nodo en el cuerpo de la clase, si es método, agregue
        for c in clase:
            for n in c.body:
                if isinstance(n, ast.FunctionDef):
                    metodos.append(n)
                    # si el método es __init__ donde están los atributos
                    if n.name == '__init__':
                        # camine to_do lo que está dentro de init
                        function_inside = ast.walk(n)
                        # si eso dentro de init es un atributo agregelo a la lista, si no, pase
                        for e in function_inside:
                            if isinstance(e, ast.Attribute):
                                listaatributos.append(e.attr)
                            if isinstance(e, ast.arguments):
                                pass
                            else:
                                pass

    # armar el grafo, por cada clase, agregue nodo clase
    for c in clase:
        clas = c.name
        # por cada método en lista métodos, agregue nodo m.name
        for m in metodos:
            metodo_nom = m.name
            # por cada argumento en argumentos, si es self, pase, si no, agregue a dicc
            for argum in m.args.args:
                if argum.arg == 'self':
                    pass
                else:
                    argum_nom = argum.arg
                    listaargumentos.append(argum_nom)
                    dicc_argum.setdefault(metodo_nom, [])
                    dicc_argum[metodo_nom].append(argum_nom)
                    g.add_node(argum_nom)

    # creación de edges, recorriendo atributos, métodos y argumentos
    for a in listaatributos:
        g.add_edge(clas, a)
    for elem in metodos:
        g.add_edge(clas, elem.name)
        if elem.name in dicc_argum:
            print("prueba", elem.name)
            for argumentos in dicc_argum[elem.name]:
                argu = str(argumentos)
                g.add_edge(elem.name, argu)

    # graficación
    pos = nx.circular_layout(g)
    plt.figure(figsize=(15, 12))
    nx.draw(g, pos, node_color='g', edgecolors='k', width=2.0, with_labels=True)
    nx.draw(g, pos, nodelist=[clas], node_color='r', with_labels=True)
    nx.draw(g, pos, nodelist=[str(n) for n in listaargumentos], node_color='#e2a0cb', with_labels=True)
    nx.draw(g, pos, nodelist=[str(n) for n in listaatributos], node_color='#a0e2d8', with_labels=True)
    # guardado de archivo
    buffer = io.BytesIO()
    plt.savefig(buffer, format="jpg")
    buffer.seek(0) #lee desde el primer byte
    return buffer.read() #retorna array

if __name__ == '__main__':
    app.run(debug = True)