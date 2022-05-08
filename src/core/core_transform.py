import pandas as pd


class CoreTransform(object):
    def __init__(self, extends_sqlalchemy=None):
        self.extends_sqlalchemy = extends_sqlalchemy

