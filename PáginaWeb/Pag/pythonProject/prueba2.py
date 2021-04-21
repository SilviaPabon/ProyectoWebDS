import io
#para realizar los nodos
import networkx as nx
#para graficar
import matplotlib.pyplot as plt
#para obtener abstract syntax tree
import ast

with open('List.py', 'rb') as code:

    code_ast = ast.parse(code.read())

    g = nx.Graph()
    lista = []
    listaatributos = []
    dict = {}

    for nodo in ast.walk(code_ast):
        for i in nodo.body:
            if isinstance(i, ast.ClassDef):
                print("class", i.name)
                clase = i.name
            else:
                pass

        if isinstance(nodo, ast.ClassDef):
            for e in nodo.body:
                print("nombre " + e.name)
                g.add_node(e.name)
                lista.append(e.name)
                if isinstance(e, ast.FunctionDef):
                    for nodes in ast.walk(e):
                        if isinstance(nodes, ast.arg):
                            if nodes.arg == 'self':
                                pass
                            else:
                                print(nodes.arg)
                                dict.setdefault(e.name, [])
                                dict[e.name].append(nodes.arg)
                                stringg = str(nodes.arg)
                                g.add_node(stringg)
                        if isinstance(nodes, ast.Attribute):
                            if e.name == 'clear':
                                print("atributo", nodes.attr)
                                g.add_node(nodes.attr)
                                listaatributos.append(nodes)


    for elem in lista:
        g.add_edge(clase, elem.name)
        if elem.name in dict:
            print("prueba", elem.name)
            for each in dict[elem.name]:
                agregar = str(each)
                g.add_edge(elem.name, agregar)

    for elem2 in listaatributos:
        g.add_edge(clase, elem2.attr)

pos = nx.spring_layout(g, scale= 2, seed=109)
plt.figure(figsize=(15, 12))
nx.draw_networkx_nodes(g, pos=pos, node_color='green')
nx.draw_networkx(g, pos=pos, nodelist=["List"], node_color='#A0CBE2', font_size=10)
nx.draw_networkx(g, pos=pos, nodelist=["object", "ob", "ListNode", "nodo"], node_color='#a0e2d8', font_size=10)
nx.draw_networkx(g, pos=pos, nodelist=["head", "tail", "inode", "size"], node_color='#e2a0cb', font_size=10)
plt.savefig("filename1.jpg")

if nodo.name == 'clear':
    print("atributo", nodo.args)
    # g.add_node(nodes.attr)
    # listaatributos.append(nodes)

for argum in nodo.args.args:
    if argum.arg == 'self':
        pass
    else:
        print("argumento", argum.arg)
        dict.setdefault(nodo.name, [])
        dict[nodo.name].append(argum.arg)
        stringg = str(argum.arg)
        g.add_node(stringg)

