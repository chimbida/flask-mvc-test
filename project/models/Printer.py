# -*- coding: utf-8 -*-
from flask import flash


class Printer(object):

    def show_string(self, text):
        if text == '':
            flash("Você não digitou nada para Imprimir na Tela")
        else:
            flash(text + "!!!")
