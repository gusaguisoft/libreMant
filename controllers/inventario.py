# -*- coding: utf-8 -*-
from gridext import *
# intente algo como
def equipos():
    formargs=dict(submit_button='Aceptar', fields=['id','idmodelo', 'matricula','nroserie', 'descripcion', 'idpropietario'])
    createargs=dict(fields=['idmodelo', 'matricula','nroserie', 'descripcion', 'idpropietario'])
    fields=[db.equipos.id, \
            db.equipos.idmodelo, \
            db.equipos.matricula, \
            db.equipos.nroserie]
    gridregs=SQLFORM.grid(db.equipos, fields=fields, formargs=formargs, createargs=createargs)
    tabla=db.equipos
    backurl=URL('equipos')
    if request.args(-2)=="new":
        strtitulo = "Nuevo " + tabla._singular
    elif request.args(-3)=="view":
        strtitulo = "Ver " + tabla._singular
    elif request.args(-3)== "edit":
        strtitulo = "Modificar " + tabla._singular
    else:
        strtitulo = tabla._plural
        backurl=URL("default","index")
    backbutton=gridbuttonext("buttonback", "Atrás", backurl)
    gridregs.append(backbutton)
    return dict(titulo=strtitulo, equipos=gridregs)

def tiposbien():
    gridregistros=SQLFORM.grid(db.tiposbien)
    return dict(tiposbien=gridregistros)

def marcas():
    gridmarcas=SQLFORM.grid(db.marcas)
    return dict(marcas=gridmarcas)

def modelos():
    gridregistros=SQLFORM.grid(db.modelos)
    return dict(modelos=gridregistros)

def propietarios():
    gridregistros=SQLFORM.grid(db.propietarios)
    return dict(propietarios=gridregistros)
