# -*- coding: utf8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgres://awsmaster:awspassword@syndicategames.ctef8qq9smlc.us-west-2.rds.amazonaws.com/cards'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

POWER_TYPES = ['elemental', 'combat', 'physical']
POWER_VALUES = ['1','2','3','4','5','6','7','8']
