# -*- coding: utf-8 -*-
# intente algo como
from gridext import *

def areas():
    if request.args(-3)=="edit":
        db.areas.idsuperior.requires=IS_IN_DB(db(db.areas.id != request.args(-1)), 'areas.id', '%(id)s - %(nombre)s')
    formargs=dict(submit_button='Aceptar')
    fields=[db.areas.id, \
            db.areas.nombre, \
            db.areas.seudonimo, \
            db.areas.abreviatura, \
            db.areas.siglas, \
            db.areas.idsuperior]
    gridareas=SQLFORM.grid(db.areas, fields=fields)
    if request.args(-2)=="new":
        strtitulo = "Nuevo Area"
        backurl=URL("areas")
    elif request.args(-3)=="view":
        strtitulo = "Ver Area"
        backurl=URL("areas")
    elif request.args(-3)=="edit":
        strtitulo = "Modificar Area"
        backurl=URL("areas")
    else:
        strtitulo = "Areas"
        backurl=URL("default","index")
    backbutton=gridbuttonext("buttonback", "Atrás", backurl)
    gridareas.append(backbutton)
    return dict(titulo=strtitulo, areas=gridareas)

def empleados():
    fields=[db.empleados.id, \
            db.empleados.nombre, \
            db.empleados.apellido, \
            db.empleados.numerodocumento, \
            db.empleados.idarea]
    formargs=dict(submit_button='Aceptar')
    gridemps=SQLFORM.grid(db.empleados, fields=fields)
    if request.args(-2)=="new":
        strtitulo = "Nuevo Empleado"
        backurl=URL("empleados")
    elif request.args(-3)=="view":
        strtitulo = "Ver Empleado"
        backurl=URL("empleados")
    elif request.args(-3)=="edit":
        strtitulo = "Modificar Empleado"
        backurl=URL("empleados")
    else:
        strtitulo = "Empleados"
        backurl=URL("default","index")
    backbutton=gridbuttonext("buttonback", "Atrás", backurl)
    gridemps.append(backbutton)
    return dict(titulo=strtitulo, empleados=gridemps)

def ubicaciones():
    fields=[db.ubicaciones.id, \
            db.ubicaciones.nombre, \
            db.ubicaciones.seudonimo, \
            db.ubicaciones.abreviatura, \
            db.ubicaciones.siglas, \
            db.ubicaciones.idsuperior]
    formargs=dict(submit_button='Aceptar')
    if request.args(-3)=="edit":
        db.ubicaciones.idsuperior.requires=IS_IN_DB(db(db.ubicaciones.id != request.args(-1)), 'ubicaciones.id', '%(id)s - %(nombre)s')
    gridubics=SQLFORM.grid(db.ubicaciones, fields=fields)
    if request.args(-2)=="new":
        strtitulo = "Nueva Ubicación"
        backurl=URL("ubicaciones")
    elif request.args(-3)=="view":
        strtitulo = "Ver Ubicación"
        backurl=URL("ubicaciones")
    elif request.args(-3)=="edit":
        strtitulo = "Modificar Ubicación"
        backurl=URL("ubicaciones")
    else:
        strtitulo = "Ubicaciones"
        backurl=URL("default","index")
    backbutton=gridbuttonext("buttonback", "Atrás", backurl)
    gridubics.append(backbutton)
    return dict(titulo=strtitulo, ubicaciones=gridubics)

def tiposdocumento():
    fields=[db.tiposdocumento.id, \
            db.tiposdocumento.nombre, \
            db.tiposdocumento.seudonimo, \
            db.tiposdocumento.abreviatura, \
            db.tiposdocumento.siglas]
    formargs=dict(submit_button='Aceptar')
    gridtiposdoc=SQLFORM.grid(db.tiposdocumento, fields=fields, formargs=formargs)
    if request.args(-2)=="new":
        strtitulo = "Nuevo Tipo de Documento"
        backurl=URL("tiposdocumento")
    elif request.args(-3)=="view":
        strtitulo = "Ver Tipo de Documento"
        backurl=URL("tiposdocumento")
    elif request.args(-3)=="edit":
        strtitulo = "Modificar Tipo de Documento"
        backurl=URL("tiposdocumento")
    else:
        strtitulo = "Tipos de Documento"
        backurl=URL("default","index")
    backbutton=gridbuttonext("buttonback", "Atrás", backurl)
    gridtiposdoc.append(backbutton)
    return dict(titulo=strtitulo, tiposdocumento=gridtiposdoc)
