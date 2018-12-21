# -*- coding: utf-8 -*-
db.define_table('tiposarea'
                ,Field('nombre', 'string', length=75, notnull=True, unique=True)
                ,Field('seudonimo', 'string', length=50, notnull=True, unique=True)
                ,Field('abreviatura', 'string', length=25, notnull=True, unique=True)
                ,Field('siglas', 'string', length=10, notnull=True, unique=True)
                ,Field('descripcion', 'string', length=150)
                ,Field('imagen', 'upload')
                ,Field('activo', 'boolean')
                ,rname='org.tiposarea'
                ,migrate=True
                ,format='%(seudonimo)s')

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
                ,Field('idtipoarea', 'reference tiposarea', label='Tipo')
                ,rname='org.areas'
                ,migrate=True
                ,format=lambda r: rutacompleta(r)) # se usa para visualizar la tabla cuando es referenciada por un campo en formularios

db.areas.imagen.requires=IS_EMPTY_OR(IS_IMAGE(extensions=('jpeg','png','bmp','gif'),maxsize=(200,200)))
# Se usa para visualizar el campo idsuperior con algun dato adicional y no solo con el número
db.areas.idsuperior.represent=lambda v,r: str('' if v is None else r.idsuperior.nombre)
# Se usa para seleccionar el campo idsuperior referenciado con algun dato más representativo que el id validando su valor
db.areas.idsuperior.requires=IS_EMPTY_OR(IS_IN_DB(db, 'areas.id', '%(id)s - %(nombre)s'))

db.define_table('empleados'
                ,Field('primernombre', 'string', length=40, notnull=True, label='Primer Nombre')
                ,Field('primerapellido', 'string', length=40, notnull=True, label='Primer Apellido')
                ,Field('segundonombre', 'string', length=40, label='Segundo Nombre')
                ,Field('segundoapellido', 'string', length=40, label='Segundo Apellido')
                ,Field('tercernombre', 'string', length=40, label='Tercer Nombre')
                ,Field('tercerapellido', 'string', length=40, label='Tercer Apellido')
                ,Field('idtipodocumento', 'reference tiposdocumento', label='Tipo de Documento')
                ,Field('numerodocumento', 'integer', notnull=False, label='N° de Documento')
                ,Field('datosfoto', 'blob', null=True)
                ,Field('foto', 'upload', null=True, uploadfield='datosfoto')
                ,Field('idarea', 'reference areas', label='Area')
                ,Field.Virtual('apellidoynombre', lambda r: r.empleados.primerapellido + ', ' + r.empleados.primernombre)
#                ,Field.Virtual('nombreyapellido', lambda r: r.empleados.primernombre + ' ' + r.empleados.primerapellido)
#                ,Field.Virtual('nombresyapellidos', lambda r: r.primernombre + ((' ' + r.segundonombre) or '') + ((' ' + r.tercernombre) or '') \
#                                                   + ' ' + r.primerapellido + ((' '+ r.segundoapellido) or '') + ((' ' + r.tercerapellido) or ''))
                ,rname='org.empleados'
                ,migrate=True
                ,format='%(primernombre)s %(primerapellido)s')

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
                ,format='%(seudonimo)s')
