# -*- coding: utf-8 -*-
from gridext import *
usuarioactual=db.auth_user[auth.user_id]
empleadoactual=db.empleados[usuarioactual.idempleado]
areaactual=db.areas[empleadoactual.idarea]

def mis_solicitudes():
    db.solicitudes.idempleadosolicitante.default=empleadoactual.id
    db.solicitudes.idareasolicitante.default=areaactual.id
    db.solicitudes.estado.default=0
    db.solicitudes.idpuesto.default=db(db.puestos.idempleado==empleadoactual.id & db.puestos.idarea==areaactual.id).select.first.id
    fields=[db.solicitudes.id, \
            db.solicitudes.fechasolicitud, \
            db.solicitudes.idtiposolicitud, \
            db.solicitudes.descripcion, \
            db.solicitudes.idpuesto, \
            db.solicitudes.estado]
    createargs=dict(fields=['id','idareasolicitante', 'idtiposolicitud', 'descripcion'],\
                    showid=False, submit_button='Registrar')
    ui=myui()
    links=[lambda row: gridbuttonext(buttonclass="buttonprint",buttontext="Imprimir",buttonurl=URL("area","imprimir",args=[row.id]))]
    query=(db.solicitudes.idempleadosolicitante==empleadoactual.id) & (db.solicitudes.idareasolicitante==areaactual.id)
    orderby=~db.solicitudes.id
    editable=lambda row: True if row.estado==0 else False
    deletable=lambda row: True if ((row.estado==0) and (not row.idtiposolicitud.autorizable)) else False
    grid=SQLFORM.grid(query=query, orderby=orderby, deletable=deletable, editable=editable, fields=fields, links=links, user_signature=False, maxtextlength=50, createargs=createargs, paginate=5, ui=ui, showbuttontext=True)
    if request.args(-2)=="new":
        strtitulo = "Nueva Solicitud"
        backurl=URL("mis_solicitudes")
    elif request.args(-3)=="view":
        strtitulo = "Ver Solicitud"
        backurl=URL("mis_solicitudes")
    elif request.args(-3)=="edit":
        strtitulo = "Modificar Solicitud"
        backurl=URL("mis_solicitudes")
    else:
        strtitulo = "Mis Solicitudes"
        backurl=URL("default","index")
    backbutton=gridbuttonext("buttonback", "Volver", backurl)
    grid.append(backbutton)
    return dict(titulo=strtitulo,solicitudes=grid)
