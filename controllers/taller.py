# -*- coding: utf-8 -*-
from gridext import *
def puestos():
    formargs=dict(submit_button='Aceptar', fields=['id', 'nombre', 'idarea', 'idubicacion', 'descripcion'])
    createargs=dict(fields=['nombre', 'idarea', 'idubicacion', 'descripcion'])
    fields=[db.puestos.id, \
            db.puestos.nombre, \
            db.puestos.idarea, \
            db.puestos.idubicacion]
    links=[lambda row: gridbuttonext("buttonprint","Equipos",URL("taller","equipospuesto",args=[row.id]))]
    gridregs=SQLFORM.grid(db.puestos, fields=fields, formargs=formargs, createargs=createargs, links=links, user_signature=False)
    tabla=db.puestos
    backurl=URL('puestos')
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
    return dict(titulo=strtitulo, puestos=gridregs)

def equipospuesto():
    # request.args(0) es id de la solicitud
    puesto=db.puestos[request.args(0)]
    addbutton=gridbuttonext("buttonadd", "Agregar", URL('equipossinpuesto'))
    
    fields=[db.equipos.id, \
            db.equipos.idmodelo, \
            db.equipos.matricula, \
            db.equipos.nroserie]
    query=(db.equipos.idpuesto==puesto.id)
    ui=myui()
    formargs=dict(fields=['id','idmodelo','matricula','nroserie'], showid=False)
    gridregs=SQLFORM.grid(query=query, \
                          fields=fields, \
                          args=request.args, \
                          searchable=False, \
                          create=True, \
                          deletable=False, \
                          user_signature=False, \
                          maxtextlength=50, \
                          formargs=formargs,\
                          ui=ui)
    tabla=db.equipos
    backurl=URL('equipospuesto')
    if request.args(-2)=="new":
        strtitulo = "Nuevo " + tabla._singular + " del Puesto"
    elif request.args(-3)=="view":
        strtitulo = "Ver " + tabla._singular + " del Puesto"
    elif request.args(-3)== "edit":
        strtitulo = "Modificar " + tabla._singular + " del Puesto"
    else:
        strtitulo = tabla._plural + " del Puesto"
        backurl=URL("default","index")
    backbutton=gridbuttonext("buttonback", "Atrás", backurl)
    gridregs.append(backbutton)
    return dict(titulo=strtitulo, puesto=puesto, equipospuesto=gridregs)

def equipossinpuesto():
    # request.args(0) es id de la solicitud
    # puesto=db.puestos[request.args(0)]
    fields=[db.equipos.id, \
            db.equipos.idmodelo, \
            db.equipos.matricula, \
            db.equipos.nroserie]
    query=(db.equipos.idpuesto==None)
    ui=myui()
    gridregs=SQLFORM.grid(query=query, \
                          fields=fields, \
                          args=request.args, \
                          searchable=True, \
                          selectable=True, \
                          user_signature=False, \
                          maxtextlength=50, \
                          formargs=formargs,\
                          ui=ui)
    backurl=URL('equipospuesto')
    backbutton=gridbuttonext("buttonback", "Atrás", backurl)
    gridregs.append(backbutton)
    return dict(titulo=strtitulo, puesto=puesto, equipospuesto=gridregs)