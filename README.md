# Sencillo script de Python para generar códigos de Barras y QR

## Autores
* [Ixen Rodríguez Pérez](ixenrp1976@gmail.com)
* [Michel Vega Fuenzalida](michel.vega.f@gmail.com)

## Instalación

Instalar dependecias de `Python`.

```bash
pip install pyqrcode
pip install pypng
pip install python-barcode
```

Crear fichero `Json` que contiene los datos para generar los códigos.

```bash
nano listado.json
```
```json
[
    { "id": 1000, "nombre": "Harry Potter", "ci": 80073100001, "area": "Gryffindor", "cargo": "Auror" },
    { "id": 1001, "nombre": "Ginny Weasley", "ci": 81081100002, "area": "Gryffindor", "cargo": "Profesora Colegio Hogwarts de Magia y Hechicería" },
    { "id": 1002, "nombre": "Ron Weasly", "ci": 80030100003, "area": "Gryffindor", "cargo": "Auror" },
    { "id": 1003, "nombre": "Hermione Granger", "ci": 79091900004, "area": "Gryffindor", "cargo": "Ministra de Magia del Reino Unido de Gran Bretaña e Irlanda del Norte" },
    { "id": 1004, "nombre": "Draco Malfoy", "ci": 80060500005, "area": "Slytherin", "cargo": "Mortífago" }
]
```

Crear `Python Script` para generar los códigos.

```bash
nano qrbar_code_generator
```
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
qrbar_code_generator - Genera códigos de Barras y QR
Copyleft (c) 2019 Ixen Rodríguez Pérez (ixenrp1976@gmail.com)
                  Michel Vega Fuenzalida (michel.vega.f@gmail.com)
"""


__version__ = "1.1"
__date__ = "2019-11-16"


import sys
if int(sys.version_info.major) < 3 or (int(sys.version_info.major) == 3 \
    and int(sys.version_info.minor) < 3):
    raise ImportError("Se requiere Python versión 3 o superior!")
import pyqrcode
import barcode
from barcode.writer import ImageWriter
import os
import json
import png


def genQRcode(texto, nombre):
    """
    método para generar códigos QR
    """
    codigo_qr = pyqrcode.create(texto)
    nombre_fichero = nombre + '_CodigoQR.png'
    codigo_qr.png(nombre_fichero, scale=8)


def genBARcode():
    """
    método para generar códigos de Barras
    `code39`, `code128`, `ean`, `ean13`, `ean8`, `gtin`, `issn`, `upc`, `upca`
    """
    BARCODE = barcode.get_barcode_class('code128')
    codigo_bar = BARCODE(str(id) + str(ci), writer=ImageWriter())
    nombre_fichero = codigo_bar.save(nombre + '_CodigoBarra')


# leer listado
listado = []
with open('listado.json', 'r') as inf:
    listado.append(json.load(inf))

# recorrer listado
for lista in listado:
    for uno in lista:
        id = uno['id']
        nombre = uno['nombre']
        ci = uno['ci']
        area = uno['area']
        cargo = uno['cargo']

        fichero = open('texto.txt', 'w')
        fichero.write("#:" + str(id))
        fichero.write("\n")
        fichero.write("NAME:" + str.upper(nombre))
        fichero.write("\n")
        fichero.write("ID:" + str(ci))
        fichero.write("\n")
        fichero.write("HOUSE:" + str.upper(area))
        fichero.write("\n")
        fichero.write("JOB:" + str.upper(cargo))
        fichero.write("\n")

        texto = open('texto.txt', 'r')
        fichero.close()

        # generar códigos de Barras y QR
        genBARcode()
        genQRcode(texto.read(), nombre)

        os.remove('texto.txt')
```

## Ejecución

```bash
python qrbar_code_generator
```

Un listado `ls *.png` devolvería.

```bash
'Draco Malfoy_CodigoBarra.png'   'Ginny Weasley_CodigoQR.png'    'Hermione Granger_CodigoBarra.png'  'Ron Weasly_CodigoQR.png'
'Draco Malfoy_CodigoQR.png'      'Harry Potter_CodigoBarra.png'  'Hermione Granger_CodigoQR.png'
'Ginny Weasley_CodigoBarra.png'  'Harry Potter_CodigoQR.png'     'Ron Weasly_CodigoBarra.png'
```

## Conclusiones

Imágenes resultantes listas para ser escaneadas.

<img src="files/Hermione Granger_CodigoQR.png" alt="QR Code" title="Hermione Granger" width="25%"/>  <img src="files/Hermione Granger_CodigoBarra.png" alt="BAR Code" title="Hermione Granger" width="25%" />

## Referencias

* [Generate QR code image with Python, Pillow, qrcode](https://note.nkmk.me/en/python-pillow-qrcode/)
* [python-barcode 0.10.0](https://pypi.org/project/python-barcode/)
* [how to generate barcode in python 3.7](https://stackoverflow.com/questions/57427243/how-to-generate-barcode-in-python-3-7)
* [How can I use a variable to generate barcode with python-barcode](https://stackoverflow.com/questions/51826802/how-can-i-use-a-variable-to-generate-barcode-with-python-barcode/51826815)

