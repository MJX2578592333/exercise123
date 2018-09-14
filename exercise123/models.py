#coding=utf-8

from django.db.models import *

class test(Model):
    tname = CharField(max_length=30)