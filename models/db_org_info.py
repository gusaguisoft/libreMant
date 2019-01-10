# -*- coding: utf-8 -*-
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

# TIPOS DE SOLICITUD
db.define_table('tipossolicitud'
                ,Field('nombre', 'string', length=75, notnull=True, unique=True)
                ,Field('seudonimo', 'string', length=50, notnull=True, unique=True)
                ,Field('abreviatura', 'string', length=25, notnull=True, unique=True)
                ,Field('siglas', 'string', length=10, notnull=True, unique=True)
                ,Field('descripcion', 'string', length=150)
                ,Field('imagen', 'upload')
                ,Field('activo', 'boolean')
                ,Field('idsuperior', 'reference tiposolicitud', label='Superior')
                ,rname='info.tipossolicitud'
                ,format='%(seudonimo)s')
db.tipossolicitud.idsuperior.represent = lambda v,r: str('' if v is None else r.idsuperior.nombre)
db.tipossolicitud.idsuperior.requires = IS_EMPTY_OR(IS_IN_DB(db, 'tipossolicitud.id', '%(id)s - %(nombre)s'))
db.tipossolicitud.imagen.requires = IS_EMPTY_OR(IS_IMAGE(extensions=('jpeg','png','bmp','gif'),maxsize=(200,200)))

# SOLICITUDES
db.define_table('solicitudes'
                ,Field('fechasolicitud', 'date', notnull=True, required=False, label='Fecha Solicitud')
                ,Field('horasolicitud', 'time', notnull=True, required=False, label='Hora Solicitud')
                ,Field('idempleadosolicitante', 'reference empleados', notnull=True, label='Solicitado por')
                ,Field('idareasolicitante', 'reference areas', notnull=True, label='Area Solicitante')
                ,Field('idtiposolicitud', 'reference tipossolicitud', notnull=True, label='Tipo') 
                ,Field('caratula', 'string', length=512, notnull=True, label='Carátula')
                ,Field('estado', 'integer', notnull=True, default=0)
                ,Field('fechaautorizacion', 'date', label='Fecha Autorización')
                ,Field('horaautorizacion', 'time', label='Hora Autorización')
                ,Field('idempleadoautorizacion', 'reference empleados', label='Autorizado por')
                ,Field('prioridad', 'integer', notnull=True, default=0)
                ,Field('comentarios', 'string', length=512)
                ,rname='info.solicitudes'
                ,migrate=True
                ,format=lambda r: '('+str(r.id)+') - ' + rutacompleta(r.idareasolicitante) + ' - ' + rutacompleta(r.idtiposolicitud))
# Los datos de los siguientes campos no los ingresa el usuario
db.solicitudes.idareasolicitante.writable=False # se establece por CF según el área del usuario logeado con el rol adecuado
db.solicitudes.idempleadosolicitante.writable=False # se establece por CF según el usuario logeado con el rol adecuado
db.solicitudes.fechasolicitud.writable=False # la establece el servidor de BD
db.solicitudes.horasolicitud.writable=False # la establece el servidor de BD
db.solicitudes.idempleadoautorizacion.writable=False # se establece por CF según el usuario logeado con el rol adecuado
db.solicitudes.fechaautorizacion.writable=False # la establece el servidor de BD
db.solicitudes.horaautorizacion.writable=False # la establece el servidor de BD
db.solicitudes.estado.writable=False # se establece por CF según la opción elegida
