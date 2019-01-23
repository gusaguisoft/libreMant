# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

#if not auth.user:
if not auth.user: 
    response.menu = [(T('Home'), False, URL('default', 'index'), [])]
else:
    response.menu = [
        (T('Home'), False, URL('default', 'index'), []),
        (T('Empleado'), False, '#',
         [
            (T('Mis Area'), False, URL('empleado', 'mi_area')),
            (T('Mis Compañeros'), False, URL('empleado', 'mis_compañeros')),
            (T('Mis Solicitudes'), False, URL('empleado', 'mis_solicitudes')),
            (T('Mis Solicitudes Registradas'), False, URL('empleado', 'mis_solicitudes_registradas')),
            (T('Mis Solicitudes Autorizadas'), False, URL('empleado', 'mis_solicitudes_autorizadas')),
            (T('Mis Solicitudes Enviadas'), False, URL('empleado', 'mis_solicitudes_enviadas')),
            (T('Mi Puesto de Trabajo'), False, URL('empleado', 'mi_puesto'))
         ]),
        (T('Area'), False, '#',
         [
            (T('Solicitudes'), False, URL('area', 'solicitudes')),
            (T('Empleados'), False, URL('area', 'empleados')),
            (T('Puestos'), False, URL('area', 'puestos')),
            (T('Autorización'), False, URL('area', 'autorizar_solicitudes'))
         ]),
        (T('Organismo'), False, '#',
         [
            (T('Areas'), False, URL('organismo', 'areas')),
            (T('Empleados'), False, URL('organismo', 'empleados')),
            (T('Ubicaciones'), False, URL('organismo', 'ubicaciones')),
            (T('Tipos de Documento'), False, URL('organismo', 'tiposdocumento'))
         ]),
        (T('Inventario'), False, '#',
         [
            (T('Equipos'), False, URL('inventario', 'equipos')),
            (T('Tipos de Bien'), False, URL('inventario', 'tiposbien')),
            (T('Marcas'), False, URL('inventario', 'marcas')),
            (T('Modelos'), False, URL('inventario', 'modelos')),
            (T('Propietarios'), False, URL('inventario', 'propietarios'))
         ]),
        (T('Taller'), False, '#',
         [
            (T('Puestos'), False, URL('taller', 'puestos')),
            (T('Gestión de Solicitudes'), False, URL('taller', 'gestionsolicitudes')),
            (T('Marcas'), False, URL('inventario', 'marcas')),
            (T('Modelos'), False, URL('inventario', 'modelos')),
            (T('Propietarios'), False, URL('inventario', 'propietarios')),
            (T('Tipos de Solicitud'), False, URL('taller', 'tipossolicitud'))
         ])
    ]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('This App'), False, '#', [
            (T('Design'), False, URL('admin', 'default', 'design/%s' % _app)),
            (T('Controller'), False,
             URL(
                 'admin', 'default', 'edit/%s/controllers/%s.py' % (_app, request.controller))),
            (T('View'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/%s' % (_app, response.view))),
            (T('DB Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/db.py' % _app)),
            (T('Menu Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/menu.py' % _app)),
            (T('Config.ini'), False,
             URL(
                 'admin', 'default', 'edit/%s/private/appconfig.ini' % _app)),
            (T('Layout'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/layout.html' % _app)),
            (T('Stylesheet'), False,
             URL(
                 'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % _app)),
            (T('Database'), False, URL(_app, 'appadmin', 'index')),
            (T('Errors'), False, URL(
                'admin', 'default', 'errors/' + _app)),
            (T('About'), False, URL(
                'admin', 'default', 'about/' + _app)),
        ]),
#        ('web2py.com', False, '#', [
#            (T('Download'), False,
#             'http://www.web2py.com/examples/default/download'),
#            (T('Support'), False,
#             'http://www.web2py.com/examples/default/support'),
#            (T('Demo'), False, 'http://web2py.com/demo_admin'),
#            (T('Quick Examples'), False,
#             'http://web2py.com/examples/default/examples'),
#            (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
#            (T('Videos'), False,
#             'http://www.web2py.com/examples/default/videos/'),
#            (T('Free Applications'),
#             False, 'http://web2py.com/appliances'),
#            (T('Plugins'), False, 'http://web2py.com/plugins'),
#            (T('Recipes'), False, 'http://web2pyslices.com/'),
#        ]),
        (T('Documentation'), False, '#', [
            (T('Online book'), False, 'http://www.web2py.com/book'),
            (T('Preface'), False,
             'http://www.web2py.com/book/default/chapter/00'),
            (T('Introduction'), False,
             'http://www.web2py.com/book/default/chapter/01'),
            (T('Python'), False,
             'http://www.web2py.com/book/default/chapter/02'),
            (T('Overview'), False,
             'http://www.web2py.com/book/default/chapter/03'),
            (T('The Core'), False,
             'http://www.web2py.com/book/default/chapter/04'),
            (T('The Views'), False,
             'http://www.web2py.com/book/default/chapter/05'),
            (T('Database'), False,
             'http://www.web2py.com/book/default/chapter/06'),
            (T('Forms and Validators'), False,
             'http://www.web2py.com/book/default/chapter/07'),
            (T('Email and SMS'), False,
             'http://www.web2py.com/book/default/chapter/08'),
            (T('Access Control'), False,
             'http://www.web2py.com/book/default/chapter/09'),
            (T('Services'), False,
             'http://www.web2py.com/book/default/chapter/10'),
            (T('Ajax Recipes'), False,
             'http://www.web2py.com/book/default/chapter/11'),
            (T('Components and Plugins'), False,
             'http://www.web2py.com/book/default/chapter/12'),
            (T('Deployment Recipes'), False,
             'http://www.web2py.com/book/default/chapter/13'),
            (T('Other Recipes'), False,
             'http://www.web2py.com/book/default/chapter/14'),
            (T('Helping web2py'), False,
             'http://www.web2py.com/book/default/chapter/15'),
            (T("Buy web2py's book"), False,
             'http://stores.lulu.com/web2py'),
        ])
        #,
#        (T('Community'), False, None, [
#            (T('Groups'), False,
#             'http://www.web2py.com/examples/default/usergroups'),
#            (T('Twitter'), False, 'http://twitter.com/web2py'),
#            (T('Live Chat'), False,
#             'http://webchat.freenode.net/?channels=web2py'),
#        ]),
    ]
