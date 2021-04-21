
#para realizar los nodos
import networkx as nx
import matplotlib.pyplot as plt
#para obtener abstract syntax tree
import ast

with open('List.py', 'r') as code:

    code_ast = ast.parse(code.read())

    g = nx.DiGraph()

    #almacenamiento apoyo
    clase = []
    metodos = []
    listaargumentos = []
    listaatributos = []
    dicc_argum = {}

    #hallar clases y métodos y agregarlos a listas
    # por cada nodo en to_do el cuerpo de lo leído, si es una clase, agregue a clase
    for nodo in code_ast.body:
        if isinstance(nodo, ast.ClassDef):
            clase.append(nodo)
        # por cada clase en clase, por cada nodo en el cuerpo de la clase, si es método, agregue
        for c in clase:
            for n in c.body:
                if isinstance(n, ast.FunctionDef):
                    metodos.append(n)
                    #si el método es __init__ donde están los atributos
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



    #armar el grafo, por cada clase, agregue nodo clase
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

    #creación de edges, recorriendo atributos, métodos y argumentos
    for a in listaatributos:
        g.add_edge(clas, a)
    for elem in metodos:
        g.add_edge(clas, elem.name)
        if elem.name in dicc_argum:
            print("prueba", elem.name)
            for argumentos in dicc_argum[elem.name]:
                argu = str(argumentos)
                g.add_edge(elem.name, argu)

    #graficación
    pos = nx.circular_layout(g)
    plt.figure(figsize=(15, 12))
    nx.draw(g, pos, node_color='g', edgecolors='k', width=2.0, with_labels=True)
    nx.draw(g, pos, nodelist=[clas], node_color='r', with_labels=True)
    nx.draw(g, pos, nodelist=[str(n) for n in listaargumentos], node_color='#e2a0cb', with_labels=True)
    nx.draw(g, pos, nodelist=[str(n) for n in listaatributos], node_color='#a0e2d8', with_labels=True)

    plt.savefig("graf.jpg")
