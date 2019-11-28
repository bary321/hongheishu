# coding:utf-8

__author__ = 'bary'

class LengthException(Exception):
    def __init__(self, err='length not equal'):
        Exception.__init__(self, err)


class RootNoBlack(Exception):
    def __init__(self, err="root not black"):
        Exception.__init__(self, err)


class HongChild(Exception):
    def __init__(self, err="child not black"):
        Exception.__init__(self, err)





















































































