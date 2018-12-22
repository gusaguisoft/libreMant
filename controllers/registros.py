# -*- coding: utf-8 -*-
# intente algo como
def marcas():
    grid=SQLFORM.grid(db.marcas)
    return dict(registros=grid)

def modelos():
    grid=SQLFORM.grid(db.modelos)
    return dict(registros=grid)

def tiposbien():
    grid=SQLFORM.grid(db.tiposbien)
    return dict(registros=grid)

def propietarios():
    grid=SQLFORM.grid(db.propietarios)
    return dict(registros=grid)
