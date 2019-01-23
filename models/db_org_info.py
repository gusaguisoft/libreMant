# -*- coding: utf-8 -*-
import datetime
# PUESTOS
db.define_table('puestos'
                ,Field('nombre', 'string', length=30, notnull=True, unique=True)
                ,Field('idarea', 'reference areas', notnull=True, label='Area')
                ,Field('idubicacion', 'reference ubicaciones', notnull=True, label='Ubicación')
                ,Field('descripcion', 'string', length=150)
                ,rname='info.puestos'
                ,singular='Puesto'
                ,plural='Puestos'
                ,format='%(nombre)s')

# PROPIETARIOS
db.define_table('propietarios'
                ,Field('nombre', 'string', length=75, notnull=True, unique=True)
                ,Field('seudonimo', 'string', length=50, notnull=True, unique=True)
                ,Field('abreviatura', 'string', length=25, notnull=True, unique=True)
                ,Field('siglas', 'string', length=10, notnull=True, unique=True)
                ,Field('descripcion', 'string', length=150)
                ,Field('imagen', 'upload')
                ,Field('activo', 'boolean')
                ,migrate=True
                ,rname='info.propietarios'
                ,format='%(seudonimo)s')


# TIPOS DE BIEN
db.define_table('tiposbien'
                ,Field('nombre', 'string', length=75, notnull=True, unique=True)
                ,Field('seudonimo', 'string', length=50, notnull=True, unique=True)
                ,Field('abreviatura', 'string', length=25, notnull=True, unique=True)
                ,Field('siglas', 'string', length=10, notnull=True, unique=True)
                ,Field('descripcion', 'string', length=150)
                ,Field('imagen', 'upload')
                ,Field('activo', 'boolean')
                ,Field('componente', 'boolean', notnull=True)
                ,rname='info.tiposbien'
                ,format='%(seudonimo)s')

# MARCAS
db.define_table('marcas'
                ,Field('nombre', 'string', length=75, notnull=True, unique=True)
                ,Field('seudonimo', 'string', length=50, notnull=True, unique=True)
                ,Field('abreviatura', 'string', length=25, notnull=True, unique=True)
                ,Field('siglas', 'string', length=10, notnull=True, unique=True)
                ,Field('descripcion', 'string', length=150)
                ,Field('imagen', 'upload')
                ,Field('activo', 'boolean')
                ,rname='info.marcas'
                ,format='%(seudonimo)s')

# MODELOS
db.define_table('modelos'
                ,Field('idtipobien', 'reference tiposbien', notnull=True, label='Tipo de Bien')
                ,Field('idmarca', 'reference marcas', notnull=True, label='Marca')
                ,Field('nombre', 'string', length=75, notnull=True, unique=True)
                ,Field('seudonimo', 'string', length=50, notnull=True, unique=True)
                ,Field('abreviatura', 'string', length=25, notnull=True, unique=True)
                ,Field('siglas', 'string', length=10, notnull=True, unique=True)
                ,Field('descripcion', 'string', length=150)
                ,Field('imagen', 'upload')
                ,Field('activo', 'boolean')
                ,rname='info.modelos'
                ,format=lambda r: r.idtipobien.abreviatura + ' ' +  r.idmarca.abreviatura + ' ' + r.nombre)

# EQUIPOS
db.define_table('equipos'
                ,Field('idmodelo', 'reference modelos', notnull=True, label='Modelo')
                ,Field('matricula', 'string', length=25, notnull=True, unique=True, label='Matrícula')
                ,Field('nroserie', 'string', length=25, label='N° Serie')
                ,Field('descripcion', 'string', length=150)
                ,Field('idpropietario', 'reference propietarios', notnull=True, label='Propietario')
                ,Field('idpuesto', 'reference puestos', label='N° Puesto')
                ,rname='info.equipos'
                ,singular='Equipo'
                ,plural='Equipos'
                ,format='%(matricula)s')


# PRIORIDADES
#db.define_table('prioridades'
#                ,Field('rotulo', 'string', length=40, notnull=True, unique=True)
#                ,Field('color', 'string', length=10, notnull=True, unique=True)
#                ,Field('imagen', 'upload')
#                ,Field('activo', 'boolean')
#                ,rname='info.prioridades'
#                ,format='%(rotulo)s')

# TIPOS DE SOLICITUD
db.define_table('tipossolicitud'
                ,Field('nombre', 'string', length=50, notnull=True, unique=True)
                ,Field('abreviatura', 'string', length=25, notnull=True, unique=True)
                ,Field('descripcion', 'string', length=150)
                ,Field('imagen', 'upload')
                ,Field('activo', 'boolean')
                ,Field('idsuperior', 'reference tipossolicitud', label='Superior')
                ,rname='info.tipossolicitud'
                ,singular='Tipo de Solicitud'
                ,plural='Tipos de Solicitud'
                ,format=lambda r: rutacompleta(r))
db.tipossolicitud.idsuperior.represent = lambda v,r: str('' if v is None else r.idsuperior.nombre)
db.tipossolicitud.idsuperior.requires = IS_EMPTY_OR(IS_IN_DB(db, 'tipossolicitud.id', '%(id)s - %(nombre)s'))
db.tipossolicitud.imagen.requires = IS_EMPTY_OR(IS_IMAGE(extensions=('jpeg','png','bmp','gif'),maxsize=(200,200)))

# SOLICITUDES
def fechahora(f, h):
    if isinstance(f, date):
        if not isinstance(h,time):
            h=datetime.time()
        return datetime.datetime.combine(f,h)
    else:
        return ''

db.define_table('solicitudes'
                ,Field('idempleadoregistro', db.empleados, notnull=True, label='Registrado por')
                ,Field('fecharegistro', 'date', notnull=True, required=False, label='Fecha Registro')
                ,Field('horaregistro', 'time', notnull=True, required=False, label='Hora Registro')
                ,Field('idareasolicitante', db.areas, notnull=True, label='Area Solicitante')
                ,Field('idtiposolicitud', db.tipossolicitud, notnull=True, label='Tipo')
                ,Field('caratula', 'string', length=100 )
                ,Field('descripcion', 'text')
                ,Field('idpuesto', db.puestos, label='Puesto')
                ,Field('estado', 'integer', notnull=True, default=0)
                ,Field('idempleadoenvio', db.empleados, label='Enviado por')
                ,Field('fechaenvio', 'date', label='Fecha Envío')
                ,Field('horaenvio', 'time', label='Hora Envío')
                ,Field.Virtual('registro', lambda r: fechahora(r.fecharegistro, r.horaregistro))
                ,Field.Virtual('envio', lambda r: fechahora(r.fechaenvio, r.horaenvio))
                ,rname='info.solicitudes'
                ,migrate=True
                ,singular='Solicitud'
                ,plural='Solicitudes'
                ,format=lambda r: '('+str(r.id)+') - ' + rutacompleta(r.idareasolicitante) + ' - ' + rutacompleta(r.idtiposolicitud))

# campos no modificables por el usuario
db.solicitudes.idempleadoregistro.writable=False # el usuario que inició sesión
db.solicitudes.idareasolicitante.writable=False # el área del usuario que inició sesión
db.solicitudes.fecharegistro.writable=False # la fecha del servidor
db.solicitudes.horaregistro.writable=False # la hora del servidor
db.solicitudes.idempleadoenvio.writable=False # el usuario que inicia sesión
db.solicitudes.fechaenvio.writable=False # la fecha del servidor
db.solicitudes.horaenvio.writable=False # la hora del servidor
db.solicitudes.estado.writable=False # estado según las operaciones realizadas en el sistema

# representación de campos
db.solicitudes.idempleadoenvio.represent=lambda value, row: apellidoynombre(row) if value else ''
db.solicitudes.fecharegistro.represent=lambda value, row: value.strftime('%d/%m/%Y') if value else ''
db.solicitudes.horaregistro.represent=lambda value, row: value.strftime('%H:%M:%S') if value else ''
db.solicitudes.fechaenvio.represent=lambda value, row: value.strftime('%d/%m/%Y') if value else ''
db.solicitudes.horaenvio.represent=lambda value, row: value.strftime('%H:%M:%S') if value else ''
db.solicitudes.registro.represent=lambda value, row: value.strftime('%d/%m/%Y %H:%M:%S') if value else ''
db.solicitudes.envio.represent=lambda value, row: value.strftime('%d/%m/%Y %H:%M:%S') if value else ''


# antes de agregar actualiza fecha y hora
def antes_agregar_solicitud(cambios):
    fechahora=datetime.datetime.now()
    cambios['fecharegistro']=datetime.date.today()
    cambios['horaregistro']=datetime.time(fechahora.hour, fechahora.minute, fechahora.second)
db.solicitudes._before_insert.append(lambda cambios: antes_agregar_solicitud(cambios))
