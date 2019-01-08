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
                ,format='%(nombre)s')

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
