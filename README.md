# Sencillo script de Python para generar Códigos de Barra y QR

```python
"""
Generador de QR y de Barras
por Michel Vega :D

https://note.nkmk.me/en/python-pillow-qrcode/

Install:
pip3 install pyqrcode
pip3 install pypng
pip3 install treepoem
"""

import pyqrcode
import treepoem
import os
import json
import png


def generate_qr(texto, name):
    """
    método que genera los ficheros con los códigos QR
    """
    codigo_qr = pyqrcode.create(texto)
    nombre_fichero = name + '_CodigoQR.png'
    codigo_qr.png(nombre_fichero, scale=8)


def generate_brcode(id, name):
    """
    método que genera los ficheros con los Código de Barras
    """
    image = treepoem.generate_barcode(
        barcode_type='code39',
        data=str(id),
    )
    nombre_fichero = name + '_CodigoBarra.png'
    image.convert('1').save(nombre_fichero)


# leer listado
listado = []
with open('listado.json', 'r') as inf:
    listado.append(json.load(inf))

# recorrer listado
for lista in listado:
    for uno in lista:
        id = uno['id']
        name = uno['name']
        ci = uno['ci']
        area = uno['area']
        cargo = uno['cargo']

        generate_brcode(ci, name)

        fichero = open('text.txt', 'w')
        fichero.write("ID:" + str(id))
        fichero.write("\n")
        fichero.write("NO:" + str.upper(name))
        fichero.write("\n")
        fichero.write("CI:" + str(ci))
        fichero.write("\n")
        fichero.write("AR:" + str.upper(area))
        fichero.write("\n")
        fichero.write("CA:" + str.upper(cargo))
        fichero.write("\n")

        texto = open('text.txt', 'r')

        fichero.close()
        os.remove('text.txt')

        generate_qr(texto.read(), name)
```

