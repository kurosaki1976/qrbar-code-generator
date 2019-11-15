# Sencillo script de Python para generar Códigos de Barra y QR

## Autor
[Michel Vega Fuenzalida](michel.vega.f@gmail.com)

## Instalación

Instalar dependecias de `Python`.

```bash
pip install pyqrcode
pip install pypng
pip install treepoem
```

Crear fichero `Json` que contiene los datos para generar los códigos.

```bash
nano listado.json
```
```json
[{ "id": 1401, "name": "Rolando Lawrence Contreras", "ci": 66121002785, "area": "Direccion", "cargo": "Director" },
{ "id": 1410, "name": "Hector Suarez Rigñack", "ci": 71072324823, "area": "Economia", "cargo": "Especialista C en Gestion Economica (EP)" },
{ "id": 1402, "name": "Maura Santiesteban Batista", "ci": 64020425355, "area": "Economia", "cargo": "Tecnico C en Gestion Economica" },
{ "id": 1403, "name": "Ana Gloria Jaime Verde", "ci": 65112605519, "area": "Capital Humano", "cargo": "Especialista C en Gestion de Capital Humano" },
{ "id": 1416, "name": "Yunaisy Hechavarria Pita", "ci": 75033105377, "area": "Mercadotecnia", "cargo": "Especialista en Ciencas Informaticas" },
{ "id": 1418, "name": "Carlos Medina Peña", "ci": 63030427364, "area": "Direccion", "cargo": "Chofer D" },
{ "id": 1408, "name": "Pedro Perez Florain", "ci": 84090729068, "area": "Comunicaciones", "cargo": "Tecnico en Ciencias Informaticas" },
{ "id": 1409, "name": "Jorge Leiva Mendez", "ci": 85032522980, "area": "Ofimatica", "cargo": "Especialista en Ciencias Informaticas" },
{ "id": 1407, "name": "Osmel Pazos Acosta", "ci": 85091229141, "area": "Telematica", "cargo": "Administrador Superior de Redes Informaticas" },
{ "id": 1405, "name": "Julio Lopez Hernandez", "ci": 86071126940, "area": "Implantacion", "cargo": "Especialista C en Ciencias Informaticas (EP)" },
{ "id": 1413, "name": "Nereida Barbara Rosa Acuña", "ci": 61121600596, "area": "Implantacion", "cargo": "Especialista en Ciencias Informaticas" },
{ "id": 1415, "name": "Ailin Hechavarria Palacios", "ci": 89090747451, "area": "Implantacion", "cargo": "Especialista en Ciencias Informaticas" },
{ "id": 1419, "name": "Michel Ernesto Vega Fuenzalida", "ci": 75110206587, "area": "Implantacion", "cargo": "Especialista en Ciencias Informaticas" }]
```

Crear `Python Script` para generar los códigos.

```bash
nano code_generator.py
```
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
code_generator.py - Genera códigos de barra y QR
Copyleft (c) 2019 Michel Vega Fuenzalida (michel.vega.f@gmail.com)
"""


__version__ = "1.0"
__date__ = "2017-08-31"


import sys
if int(sys.version_info.major) < 3 or (int(sys.version_info.major) == 3 \
    and int(sys.version_info.minor) < 3):
    raise ImportError("Se requiere Python versión 3 o superior")
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

## Referencias
* [Generate QR code image with Python, Pillow, qrcode](https://note.nkmk.me/en/python-pillow-qrcode/)

