# -*- coding: utf8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = ''
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5
