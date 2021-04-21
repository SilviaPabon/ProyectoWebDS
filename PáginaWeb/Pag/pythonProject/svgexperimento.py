import io

from bs4 import BeautifulSoup

def tocode(bytesvg):
    with bytesvg as svgimg:

        f = io.StringIO()

        # escaneando dentro del documento con BeautifulSoup
        soup = BeautifulSoup(svgimg, "html.parser")
        setellipse = soup.find('g')
        nodes = setellipse.find_all('text')
        print(nodes)

        listaatributos = []
        listacolores = []
        sumaatributos = ""
        # condicionales por colores
        # revisar con un diccionario

        for node in nodes:
            color = node['fill']
            if color == '#FFB570':
                f.write('class ' + node.get_text() + ":" + '\n')
            if color == '#A0E2D8':
                listaatributos.append(node.get_text())

        for atrib in listaatributos:
            sumaatributos += '        self.' + atrib + " = None" + '\n'
        f.write('    def ' + "__init__" + "(self):" + '\n')
        f.write(sumaatributos)

        for node in nodes:
            color = node['fill']
            print(color)
            if color == '#087D0B':
                f.write('    def ' + node.get_text() + "(self):")
                f.write('\n' + "        pass" + '\n')

        f.seek(0)
        return f