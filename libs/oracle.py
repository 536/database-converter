# !/usr/bin/env python3
# coding: utf-8
import cx_Oracle

import settings

conn = cx_Oracle.connect(
    settings.ORACLE_USERNAME,
    settings.ORACLE_PASSWORD,
    '{}:{}/{}'.format(
        settings.ORACLE_HOST,
        int(settings.ORACLE_PORT),
        settings.ORACLE_DB,
    ),
    encoding='UTF-8',
    nencoding='UTF-8'
)

__all__ = ['conn']
