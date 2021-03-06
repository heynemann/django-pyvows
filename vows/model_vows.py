#!/usr/bin/python
# -*- coding: utf-8 -*-

# django-pyvows extensions
# https://github.com/rafaelcaricio/django-pyvows

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Rafael Caricio rafael@caricio.com

from pyvows import Vows, expect
from django_pyvows.context import DjangoContext

DjangoContext._start_environment('sandbox.settings')

from sandbox.main.models import StringModel

@Vows.batch
class ModelVows(Vows.Context):

    class MainModel(DjangoContext):

        def topic(self):
            return self._model(StringModel)

        def should_be_cruddable_when_model_only_has_a_string(self, topic):
            expect(topic).to_be_cruddable()

        def should_be_cruddable_when_string_passed(self, topic):
            expect(topic).to_be_cruddable({
                'name': 'something'
            })


