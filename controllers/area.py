# -*- coding: utf-8 -*-
from gridext import *
import datetime
usuarioactual=db.auth_user[auth.user_id]
empleadoactual=db.empleados[usuarioactual.idempleado]
areaactual=db.areas[empleadoactual.idarea]

def solicitudes():
    db.solicitudes.idareasolicitante.default=areaactual.id
    db.solicitudes.estado.default=0
    #db.solicitudes.idpuesto.default=db(db.puestos.idempleado==empleadoactual.id & db.puestos.idarea==areaactual.id).select.first.id
    fields=[db.solicitudes.id, \
            db.solicitudes.fecharegistro, \
            db.solicitudes.idempleadoregistro, \
            db.solicitudes.idtiposolicitud, \
            db.solicitudes.caratula, \
            db.solicitudes.idpuesto, \
            db.solicitudes.fechaautorizacion, \
            db.solicitudes.idempleadoautorizacion, \
            db.solicitudes.fechaenvio, \
            db.solicitudes.idempleadoenvio, \
            db.solicitudes.estado]
    #qpuestos=db.puestos.idarea==areaactual.id
    createargs=dict(fields=['id','idareasolicitante', 'idtiposolicitud', 'descripcion', 'idpuesto'],\
                    showid=False, submit_button='Enviar')
    #db.solicitudes.idpuesto.requires = IS_EMPTY_OR(IS_IN_DB(db.puestos.idarea==areaactual.id, db.puestos.id))
    db.solicitudes.idpuesto.requires = IS_EMPTY_OR(IS_IN_DB(db(db.puestos.idarea==areaactual.id), 'puestos.id', '%(nombre)s'))
    ui=myui()
    links=[lambda row: gridbuttonext(buttonclass="buttonprint",buttontext="Imprimir",buttonurl=URL("area","imprimir",args=[row.id]))]
    solicitudes_area=(db.solicitudes.idareasolicitante==areaactual.id)
    no_autorizables=(db.solicitudes.estado==0) & (db.solicitudes.idtiposolicitud.autorizable==False) 
    autorizables=(db.solicitudes.estado==0) & (db.solicitudes.idtiposolicitud.autorizable==True) 
    autorizadas=(db.solicitudes.estado==1)
    enviadas=(db.solicitudes.estado==2)
    recibidas=(db.solicitudes.estado==3)
    gestionadas=(db.solicitudes.estado==4)
    cumplidas=(db.solicitudes.estado==5)
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
