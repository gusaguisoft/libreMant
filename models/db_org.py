# -*- coding: utf-8 -*-
def nombreyapellido(r):
    return (r.nombre or '') + ' ' + (r.apellido or '')

db.define_table('tiposdocumento'
                ,Field('nombre', 'string', length=75, notnull=True, unique=True)
                ,Field('seudonimo', 'string', length=50, notnull=True, unique=True)
                ,Field('abreviatura', 'string', length=25, notnull=True, unique=True)
                ,Field('siglas', 'string', length=10, notnull=True, unique=True)
                ,Field('descripcion', 'string', length=150)
                ,Field('imagen', 'upload')
                ,Field('activo', 'boolean')
                ,rname='org.tiposdocumento'
                ,migrate=True
                ,format='%(seudonimo)s')

db.define_table('areas'
                ,Field('nombre', 'string', length=75, notnull=True, unique=True)
                ,Field('seudonimo', 'string', length=50, notnull=True, unique=True)
                ,Field('abreviatura', 'string', length=25, notnull=True, unique=True)
                ,Field('siglas', 'string', length=10, notnull=True, unique=True)
                ,Field('descripcion', 'string', length=150)
                ,Field('imagen', 'upload')
                ,Field('activo', 'boolean')
                ,Field('idsuperior', 'reference areas', label='Superior')
                ,rname='org.areas'
                ,migrate=True
                ,plural="Tipos de Area"
                ,format=lambda r: rutacompleta(r)) # se usa para visualizar la tabla cuando es referenciada por un campo en formularios

db.areas.imagen.requires=IS_EMPTY_OR(IS_IMAGE(extensions=('jpeg','png','bmp','gif'),maxsize=(200,200)))
# Se usa para visualizar el campo idsuperior con algun dato adicional y no solo con el número
db.areas.idsuperior.represent=lambda v,r: str('' if v is None else r.idsuperior.nombre)
# Se usa para seleccionar el campo idsuperior referenciado con algun dato más representativo que el id validando su valor
db.areas.idsuperior.requires=IS_EMPTY_OR(IS_IN_DB(db, 'areas.id', '%(id)s - %(nombre)s'))

db.define_table('empleados'
                ,Field('nombre', 'string', length=40, notnull=True, label='Nombre')
                ,Field('apellido', 'string', length=40, notnull=True, label='Apellido')
                ,Field('idtipodocumento', 'reference tiposdocumento', label='Tipo Doc.')
                ,Field('numerodocumento', 'integer', notnull=False, label='N° Doc.')
                ,Field('datosfoto', 'blob', null=True)
                ,Field('foto', 'upload', null=True, uploadfield='datosfoto')
                ,Field('idarea', 'reference areas', label='Area')
                ,Field.Virtual('apellidoynombre', lambda r: r.empleados.apellido + ', ' + r.empleados.nombre)
                ,Field.Virtual('nombreyapellido', lambda r: r.empleados.nombre + ' ' + r.empleados.apellido)
                ,rname='org.empleados'
                ,migrate=True
                ,format=lambda r:nombreyapellido(r))

db.define_table('ubicaciones'
                ,Field('nombre', 'string', length=75, notnull=True, unique=True)
                ,Field('seudonimo', 'string', length=50, notnull=True, unique=True)
                ,Field('abreviatura', 'string', length=25, notnull=True, unique=True)
                ,Field('siglas', 'string', length=10, notnull=True, unique=True)
                ,Field('descripcion', 'string', length=150)
                ,Field('imagen', 'upload')
                ,Field('activo', 'boolean')
                ,Field('idsuperior', 'reference ubicaciones', label='Superior')
                ,rname='org.ubicaciones'
                ,migrate=True
                ,format=lambda r: rutacompleta(r))

db.ubicaciones.imagen.requires=IS_EMPTY_OR(IS_IMAGE(extensions=('jpeg','png','bmp','gif'),maxsize=(200,200)))
# Se usa para visualizar el campo idsuperior con algun dato adicional y no solo con el número
db.ubicaciones.idsuperior.represent=lambda v,r: str('' if v is None else r.idsuperior.nombre)
# Se usa para seleccionar el campo idsuperior referenciado con algun dato más representativo que el id validando su valor
db.ubicaciones.idsuperior.requires=IS_EMPTY_OR(IS_IN_DB(db, 'ubicaciones.id', '%(id)s - %(nombre)s'))
