# -*- coding: utf-8 -*-
def rutacompleta(reg):
    if reg.idsuperior==None:
        ruta = reg.abreviatura
    else:
        ruta = rutacompleta(reg.idsuperior) + ' > ' + reg.abreviatura
    return ruta
