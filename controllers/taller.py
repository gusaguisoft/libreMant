# -*- coding: utf-8 -*-
from gridext import *
def puestos():
    formargs=dict(submit_button='Aceptar', fields=['id', 'nombre', 'idarea', 'idubicacion', 'descripcion'])
    createargs=dict(fields=['nombre', 'idarea', 'idubicacion', 'descripcion'])
    fields=[db.puestos.id, \
            db.puestos.nombre, \
            db.puestos.idarea, \
            db.puestos.idubicacion]
    links=[lambda row: gridbuttonext("buttonprint","Equipos",URL("taller","equipos_puesto",args=[row.id]))]
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
    backbutton=gridbuttonext("buttonback", "Volver", backurl)
    gridregs.append(backbutton)
    return dict(titulo=strtitulo, puestos=gridregs)

def equipos_puesto():
    # request.args(0) es el id del puesto
    puesto=db.puestos[request.args(0)]
    addbutton=gridbuttonext("buttonadd", "Agregar", URL('equipossinpuesto'))
    fields=[db.equipos.id, \
            db.equipos.idmodelo, \
            db.equipos.matricula, \
            db.equipos.nroserie]
    query=(db.equipos.idpuesto==puesto.id)
    ui=myui()
    formargs=dict(fields=['id','idmodelo','matricula','nroserie'])
    createargs=dict(showid=False)
    gridregs=SQLFORM.grid(query=query, \
                          fields=fields, \
                          args=request.args, \
                          searchable=False, \
                          create=True, \
                          deletable=False, \
                          user_signature=False, \
                          maxtextlength=50, \
                          formargs=formargs,\
                          createargs=createargs,\
                          csv=False, \
                          ui=ui)
    addbutton=gridbuttonext("buttonadd", "Agregar Equipos", URL('equipos_sin_puesto',args=(request.args(0))))
    #gridregs.insert(0, addbutton)
    gridregs[0].insert(1, addbutton)
    tabla=db.equipos
    backurl=URL('equipos_puesto')
    if request.args(-2)=="new":
        strtitulo = "Nuevo " + tabla._singular + " del Puesto"
    elif request.args(-3)=="view":
        strtitulo = "Ver " + tabla._singular + " del Puesto"
    elif request.args(-3)== "edit":
        strtitulo = "Modificar " + tabla._singular + " del Puesto"
    else:
        strtitulo = tabla._plural + " del Puesto"
        backurl=URL("default","index")
    backbutton=gridbuttonext("buttonback", "Volver", backurl)
    gridregs.append(backbutton)
    return dict(titulo=strtitulo, puesto=puesto, equipospuesto=gridregs)

def equipos_sin_puesto():
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
                          selectable=lambda ids:redirect(URL('agregar_equipos_puesto',\
                                                             args=(request.args(0),'preguntar'),\
                                                             vars=dict(ids=ids))),
                          user_signature=False, \
                          maxtextlength=50, \
                          create=False,
                          deletable=False,
                          editable=False,
                          csv=False,
                          ui=ui)
    backbutton=gridbuttonext("buttonback", "Volver", URL('equipos_puesto'))
    gridregs.append(backbutton)
    return dict(equiposasignables=gridregs)

def agregar_equipos_puesto():
    # request.args(0) es id del puesto
    puesto=db.puestos[request.args(0)]
    fields=[db.equipos.id, \
            db.equipos.idmodelo, \
            db.equipos.matricula, \
            db.equipos.nroserie]
    if isinstance(request.vars.ids, list):
        query=(db.equipos.id.belongs(request.vars.ids))
    else:
        query=(db.equipos.id==request.vars.ids)
    if request.args(1)=='hacer':
        titulo="Equipos agregados al Puesto"
        for equipo in db(query).select():
            equipo.update_record(idpuesto=puesto.id)
    else:
        titulo="Agregar Equipos al Puesto"
    ui=myui()
    gridregs=SQLFORM.grid(query=query, fields=fields, args=request.args, searchable=False, create=False, deletable=False, editable=False,                      sortable=False, details=False, csv=False, ui=ui)
    if request.args(1)=='preguntar':
        confbutton=gridbuttonext("buttoncheck", "Confirmar", URL('agregar_equipos_puesto',args=(puesto.id, 'hacer'),vars=request.vars))
        gridregs.append(confbutton)
    backbutton=gridbuttonext("buttonback", "Volver", URL('equipos_puesto', args=(puesto.id)))
    gridregs.append(backbutton)
    return dict(titulo=titulo, puesto=puesto, equipos=gridregs)

def puestosx():
    formargs=dict(submit_button='Aceptar', fields=['id', 'nombre', 'idarea', 'idubicacion', 'descripcion'])
    createargs=dict(fields=['nombre', 'idarea', 'idubicacion', 'descripcion'])
    fields=[db.puestos.id, \
            db.puestos.nombre, \
            db.puestos.idarea, \
            db.puestos.idubicacion]
    gridregs=SQLFORM.smartgrid(db.puestos, fields=fields, formargs=formargs, createargs=createargs, user_signature=False)
    return dict(puestos=gridregs)
