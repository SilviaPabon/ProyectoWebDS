html_doc = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="261px" height="171px" viewBox="-0.5 -0.5 261 171"><defs/><g><ellipse cx="135" cy="35" rx="35" ry="35" fill="#ffffff" stroke="#000000" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 68px; height: 1px; padding-top: 35px; margin-left: 101px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #FFB570; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">clase</div></div></div></foreignObject><text x="135" y="39" fill="#FFB570" font-family="Helvetica" font-size="12px" text-anchor="middle">clase</text></switch></g><ellipse cx="35" cy="135" rx="35" ry="35" fill="#ffffff" stroke="#000000" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 68px; height: 1px; padding-top: 135px; margin-left: 1px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #7EA6E0; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">atrib1</div></div></div></foreignObject><text x="35" y="139" fill="#7EA6E0" font-family="Helvetica" font-size="12px" text-anchor="middle">atrib1</text></switch></g><ellipse cx="225" cy="135" rx="35" ry="35" fill="#ffffff" stroke="#000000" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 68px; height: 1px; padding-top: 135px; margin-left: 191px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #7EA6E0; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">atrib2</div></div></div></foreignObject><text x="225" y="139" fill="#7EA6E0" font-family="Helvetica" font-size="12px" text-anchor="middle">atrib2</text></switch></g><path d="M 35 100 L 105.65 54.07" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 225 100 L 159.75 59.75" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="stroke"/></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://www.diagrams.net/doc/faq/svg-export-text-problems" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Viewer does not support full SVG 1.1</text></a></switch></svg>"""

from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_doc, 'html.parser')


#print(len(soup.find_all("ellipse")))
f = open("prueba.txt", "w")

soup = BeautifulSoup(html_doc, "html.parser")
setellipse = soup.find('g')
nodes = setellipse.find_all('text')

for node in nodes:
    color = node['fill']
    print(color)
    if color == '#FFB570':
        f.write('class ' + node.get_text() + ":"+'\n')
    if color == '#7EA6E0':
        f.write('    def ' + node.get_text() + "():")
        f.write('\n' + "        pass" + '\n')
f.close()
