import os

__author__ = 'jslvtr'

DEBUG = True
ADMINS = frozenset([
    os.environ.get("ADMIN_EMAIL")
])
