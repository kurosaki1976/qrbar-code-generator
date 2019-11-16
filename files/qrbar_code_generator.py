#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
qrbar_code_generator - Genera códigos de Barra y QR
Copyleft (c) 2019 Michel Vega Fuenzalida (michel.vega.f@gmail.com)
                  Ixen Rodríguez Pérez (ixenrp1976@gmail.com)

pip install pyqrcode
pip install pypng
pip install python-barcode
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
