# -*- coding: utf-8 -*-
from gridext import *
import datetime
usuarioactual=db.auth_user[auth.user_id]
empleadoactual=db.empleados[usuarioactual.idempleado]
areaactual=db.areas[empleadoactual.idarea]
query_empleadoactual = (db.solicitudes.idempleadoregistro==empleadoactual.id)
query_areaactual = (db.solicitudes.idareasolicitante==areaactual.id)
def mis_solicitudes_registradas():
    db.solicitudes.idempleadoregistro.default=empleadoactual.id
    db.solicitudes.idareasolicitante.default=areaactual.id
    db.solicitudes.estado.default=0
    #db.solicitudes.idpuesto.default=db(db.puestos.idempleado==empleadoactual.id & db.puestos.idarea==areaactual.id).select.first.id
    fields=[db.solicitudes.id, \
            db.solicitudes.fecharegistro, \
            db.solicitudes.idtiposolicitud, \
            db.solicitudes.caratula, \
            db.solicitudes.idpuesto]
    formargs=dict(fields=['id', 'idtiposolicitud', 'caratula', 'idpuesto', 'descripcion'], submit_button='Registrar') 
    createargs=dict(showid=False)
    db.solicitudes.idpuesto.requires = IS_EMPTY_OR(IS_IN_DB(db(db.puestos.idarea==areaactual.id), 'puestos.id', '%(id)s - %(nombre)s'))
    ui=myui()
    links=[lambda row: gridbuttonext(buttonclass="buttonsend",buttontext="Enviar",buttonurl=URL("enviar_solicitud",args=[row.id]))]
    query=query_empleadoactual & query_areaactual & (db.solicitudes.estado==0)
    orderby=~db.solicitudes.id
    grid=SQLFORM.grid(query=query, orderby=orderby, deletable=True, editable=True, fields=fields, links=links, user_signature=False, maxtextlength=50, formargs=formargs, createargs=createargs, paginate=5, ui=ui, showbuttontext=True)
    if request.args(-2)=="new":
        strtitulo = "Nueva Solicitud"
        backurl=URL("mis_solicitudes_registradas")
    elif request.args(-3)=="view":
        strtitulo = "Ver Solicitud"
        backurl=URL("mis_solicitudes_registradas")
    elif request.args(-3)=="edit":
        strtitulo = "Modificar Solicitud"
        backurl=URL("mis_solicitudes_registradas")
    else:
        strtitulo = "Mis Solicitudes Registradas"
        backurl=URL("default","index")
    backbutton=gridbuttonext("buttonback", "Volver", backurl)
    grid.append(backbutton)
    return dict(titulo=strtitulo,solicitudes=grid)

def mis_solicitudes_enviadas():
    db.solicitudes.idempleadoregistro.default=empleadoactual.id
    db.solicitudes.idareasolicitante.default=areaactual.id
    #db.solicitudes.idpuesto.default=db(db.puestos.idempleado==empleadoactual.id & db.puestos.idarea==areaactual.id).select.first.id
    fields=[db.solicitudes.id, \
            db.solicitudes.fecharegistro, \
            db.solicitudes.idtiposolicitud, \
            db.solicitudes.caratula, \
            db.solicitudes.idpuesto, \
            db.solicitudes.fechaenvio, \
            db.solicitudes.estado]
    ui=myui()
    links=[lambda row: gridbuttonext(buttonclass="buttonprint",buttontext="Seguir",buttonurl=URL("empleado","seguir_solicitud",args=[row.id]))]
    query=query_empleadoactual & query_areaactual & (db.solicitudes.estado>=1)
    orderby=~db.solicitudes.id
    grid=SQLFORM.grid(query=query, orderby=orderby, create=False, deletable=False, editable=False, fields=fields, links=links, user_signature=False, maxtextlength=50, paginate=5, ui=ui, showbuttontext=True)
    if request.args(-2)=="new":
        strtitulo = "Nueva Solicitud"
        backurl=URL("mis_solicitudes_enviadas")
    elif request.args(-3)=="view":
        strtitulo = "Ver Solicitud"
        backurl=URL("mis_solicitudes_enviadas")
    elif request.args(-3)=="edit":
        strtitulo = "Modificar Solicitud"
        backurl=URL("mis_solicitudes_enviadas")
    else:
        strtitulo = "Mis Solicitudes Enviadas"
        backurl=URL("default","index")
    backbutton=gridbuttonext("buttonback", T("Back"), backurl)
    grid.append(backbutton)
    return dict(titulo=strtitulo,solicitudes=grid)

def enviar_solicitud():
    solicitud=db.solicitudes[request.args(0)]
    solicitud.update(estado=1)
    fields=['id', 'idtiposolicitud', 'caratula', 'idpuesto', 'descripcion']
    db.solicitudes.idtiposolicitud.writable=False
    db.solicitudes.caratula.writable=False
    db.solicitudes.idpuesto.writable=False
    db.solicitudes.descripcion.writable=False
    form=SQLFORM(db.solicitudes, solicitud, fields=fields)
    backbutton=gridbuttonext("buttonback", T("Back"),URL("mis_solicitudes_registradas"))
    form.append(backbutton)
    if form.process().accepted:
        response.flash = 'Se ha enviado la solicitud'
        redirect(URL("detalle_envio", args=(form.vars.id)))
    elif form.errors:
        response.flash = 'Se han producido errores al intentar enviar la solicitud'
    else:
        response.flash = 'Verifique los datos del envío y luego presione Enviar'
    return dict(solicitud_a_enviar=form)

def detalle_envio():
    solicitud=db.solicitudes[request.args(0)]
    fields=['id', 'envio', 'idempleadoenvio', 'idtiposolicitud', 'caratula', 'idpuesto', 'descripcion']
    form=SQLFORM(db.solicitudes, solicitud, fields=fields, readonly=True)
    backbutton=gridbuttonext("buttonback", T("Back"),URL("mis_solicitudes_registradas"))
    form.append(backbutton)
    return dict(solicitud_enviada=form)
