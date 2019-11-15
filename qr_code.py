#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pineMailcop - Genera /etc/postfix/postfwd.cf
Copyleft (c) 2019 Michel Vega Fuenzalida (michel.vega.f@gmail.com)
"""


__version__ = "1.0"
__date__ = "2019-11-14"


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
