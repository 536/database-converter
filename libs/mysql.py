# !/usr/bin/env python3
# coding: utf-8
import pymysql

import settings

conn = pymysql.connect(
    host=settings.MYSQL_HOST,
    port=int(settings.MYSQL_PORT),
    user=settings.MYSQL_USERNAME,
    password=settings.MYSQL_PASSWORD,
    db=settings.MYSQL_DB,
    charset=settings.MYSQL_CHARSET,
)

__all__ = ['conn']
