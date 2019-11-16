# Sencillo script de Python para generar Códigos de Barra y QR

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
[{ "id": 1000, "nombre": "Ixen Rodríguez Pérez", "ci": 19111678901, "area": "Informática", "cargo": "Especialista B Ciencias Informáticas" },
{ "id": 1001, "nombre": "Misleydi Ferguson Jimenez", "ci": 19111678902, "area": "Informática", "cargo": "Técnica Ciencias Informáticas" },
{ "id": 1002, "nombre": "Aizen Rodríguez Ferguson", "ci": 19111678903, "area": "Primaria", "cargo": "Alumno 2do grado" },
{ "id": 1003, "nombre": "Aiza Rodríguez Ferguson", "ci": 19111678904, "area": "Circulo Infantil", "cargo": "Tercer año de vida" }]
```

Crear `Python Script` para generar los códigos.

```bash
nano qrbar_code_generator
```
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
qrbar_code_generator - Genera códigos de Barra y QR
Copyleft (c) 2019 Michel Vega Fuenzalida (michel.vega.f@gmail.com)
                  Ixen Rodríguez Pérez (ixenrp1976@gmail.com)
"""


__version__ = "1.1"
__date__ = "2019-11-16"


import sys
if int(sys.version_info.major) < 3 or (int(sys.version_info.major) == 3 \
    and int(sys.version_info.minor) < 3):
    raise ImportError("Se requiere Python versión 3 o superior")
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

        genBARcode()

        fichero = open('texto.txt', 'w')
        fichero.write("ID:" + str(id))
        fichero.write("\n")
        fichero.write("NO:" + str.upper(nombre))
        fichero.write("\n")
        fichero.write("CI:" + str(ci))
        fichero.write("\n")
        fichero.write("AR:" + str.upper(area))
        fichero.write("\n")
        fichero.write("CA:" + str.upper(cargo))
        fichero.write("\n")

        texto = open('texto.txt', 'r')

        fichero.close()
        os.remove('texto.txt')

        genQRcode(texto.read(), nombre)
```

## Ejecución

```bash
python qrbar_code_generator
```

## Referencias
* [Generate QR code image with Python, Pillow, qrcode](https://note.nkmk.me/en/python-pillow-qrcode/)

