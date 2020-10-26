# !/usr/bin/env python3
# coding: utf-8
import os

import settings
from libs.mysql import conn as mysql_conn
from libs.oracle import conn as oracle_conn

from settings import logger

# 防止读取结果出现中文乱码（问号）情况
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


def to_str(string):
    if string is None:
        return "''"
    else:
        return "'" + str(string) + "'"


def main():
    try:  # 从Oracle读取
        with oracle_conn.cursor() as cursor:
            cursor.execute(settings.SELECT_SQL)
            fields = cursor.description
            contents = cursor.fetchall()
        logger.info('Success to read from Oracle.')
    except Exception as e:
        logger.warning('Failed to read from Oracle.')
        logger.exception(e)
    finally:
        oracle_conn.close()

    try:  # 写入MySQL
        with mysql_conn.cursor() as cursor:
            sql = "insert into {} ({}) values {}".format(
                settings.INSERT_INTO_TABLE,
                ', '.join([field[0] for field in fields]),
                ', '.join(map(lambda x: '(' + x + ')',
                              [', '.join(map(lambda s: to_str(s), content)) for content in contents]))
            )
            logger.info(sql)
            cursor.execute(sql)
            mysql_conn.commit()
        logger.info('Success to insert into MySQL.')
    except Exception as e:
        logger.warning('Failed to insert into MySQL.')
        logger.exception(e)
    finally:
        mysql_conn.close()


if __name__ == '__main__':
    main()
