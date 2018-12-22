#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *

def myuiext():
    return dict(buttonprint='fas fa-print', \
                buttonup='fas fa-arrow-alt-circle-up', \
                buttondown='fas fa-arrow-alt-circle-down', \
                buttonright='fas fa-arrow-alt-circle-right', \
                buttondetails='fas fa-list-alt', \
                buttoncheck='fas fa-check-square', \
                buttonuncheck='fas fa-times-circle', \
                buttonok='fas fa-thumbs-up', \
                buttoncancel='fas fa-thumbs-down', \
                buttonsend='fas fa-share-square', \
                buttonminus='fas fa-minus-square')
def myui():
    return dict(widget='', \
                header='', \
                content='', \
                default='', \
                cornerall='', \
                cornertop='', \
                cornerbottom='', \
                button='button btn btn-default',
                buttontext='buttontext button',
                buttonadd='fas fa-plus-square', \
                buttonback='fas fa-arrow-alt-circle-left', \
                buttonexport='fas fa-file-export', \
                buttondelete='fas fa-trash-alt', \
                buttonedit='fas fa-pen-square', \
                buttontable='fas fa-table', \
                buttonview='fas fa-eye')

def gridbuttonext(buttonclass='buttonadd', buttontext=current.T('Add'), buttonurl=URL(), title=None, \
                  callback=None, delete=None, trap=True, noconfirm=None, showtext=True, background=False):
    ui=myui().copy()
    ui.update(myuiext())
    if background==True:
        keys=ui.keys()
        for key in keys:
            ui[key]=ui[key]+' fdo'
    return A(SPAN(_class=ui.get(buttonclass), _title=title or current.T(buttontext)), CAT(' '), \
             SPAN(current.T(buttontext), _title=title or current.T(buttontext), _class=ui.get('buttontext')),
             _href=buttonurl, \
             callback=callback, \
             delete=delete, \
             noconfirm=noconfirm, \
             _class=ui.get('button'))
