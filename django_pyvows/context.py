#!/usr/bin/python
# -*- coding: utf-8 -*-

# django-pyvows extensions
# https://github.com/rafaelcaricio/django-pyvows

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Rafael Caricio rafael@caricio.com

import os

from pyvows import Vows
from django_pyvows.assertions import Url
from django_pyvows.model_assertions import Model
from django.http import HttpRequest

class DjangoContext(Vows.Context):
    @classmethod
    def _start_environment(cls, settings_path):
        if not settings_path:
            raise RuntimeError('The settings_path argument is required.')
        os.environ['DJANGO_SETTINGS_MODULE'] = settings_path

    def __init__(self, parent):
        super(DjangoContext, self).__init__(parent)

        from django.test.utils import setup_test_environment #, teardown_test_environment

        setup_test_environment()

    def _url(self, path):
        return Url(self, path)

    def _request(self, **kw):
        return HttpRequest(**kw)

    def _model(self, model_class):
        return Model(self, model_class)
