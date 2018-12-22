# -*- coding: utf-8 -*-
# intente algo como
def areas():
    areas=SQLFORM.grid(db.areas)
    return dict(areas=areas)

def empleados():
    empleados=SQLFORM.grid(db.empleados)
    return dict(empleados=empleados)

def ubicaciones():
    ubicaciones=SQLFORM.grid(db.ubicaciones)
    return dict(ubicaciones=ubicaciones)

def tiposarea():
    tiposarea=SQLFORM.grid(db.tiposarea)
    return dict(tipos=tiposarea)

def tiposdocumento():
    grid=SQLFORM.grid(db.tiposdocumento)
    return dict(grid=grid)
