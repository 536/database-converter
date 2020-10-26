# !/usr/bin/env python3
# coding: utf-8
import datetime
import logging
import os

import dotenv

dotenv.load_dotenv(dotenv_path='.env')

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

fh = logging.FileHandler('{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%d')), mode='w')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(fh)
logger.addHandler(ch)

ORACLE_HOST = os.getenv('ORACLE_HOST')
ORACLE_PORT = os.getenv('ORACLE_PORT')
ORACLE_USERNAME = os.getenv('ORACLE_USERNAME')
ORACLE_PASSWORD = os.getenv('ORACLE_PASSWORD')
ORACLE_DB = os.getenv('ORACLE_DB')

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')
MYSQL_CHARSET = os.getenv('MYSQL_CHARSET')

SELECT_SQL = os.getenv('SELECT_SQL')
INSERT_INTO_TABLE = os.getenv('INSERT_INTO_TABLE')
